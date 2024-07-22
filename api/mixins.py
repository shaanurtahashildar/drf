from .permissions import IsStaffEditoPermissions
from rest_framework import permissions
class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditoPermissions]