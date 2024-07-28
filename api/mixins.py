from .permissions import IsStaffEditoPermissions
from rest_framework import permissions
class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditoPermissions]


class UserQuerySetMixin():
    user_field = 'user'
    allow_staff_view =False
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data ={}
        lookup_data[self.user_field] = self.request.user
        query = super().get_queryset(*args, **kwargs)
        if self.allow_staff_view and user.is_staff:
            return query
        print(query)
        return query.filter(**lookup_data)