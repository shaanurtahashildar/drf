from rest_framework import permissions

class IsStaffEditoPermissions(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):#app_name.verb_model_name
        perms_map = {
            'GET': ['%(app_label)s.view_%(model_name)s'],
            'OPTIONS': [],
            'HEAD': [],
            'POST': ['%(app_label)s.add_%(model_name)s'],
            'PUT': ['%(app_label)s.change_%(model_name)s'],
            'PATCH': ['%(app_label)s.change_%(model_name)s'],
            'DELETE': ['%(app_label)s.delete_%(model_name)s'],
        }

        user=request.user
        print(user.get_all_permissions())
        if not user.is_staff: #admin has permissions
            return False

        return super().has_permission(request, view)
        # if user.is_staff:
        #     if user.has_perm("products.add_product"):
        #         return True
        #     if user.has_perm("products.change_product"):
        #         return True
        #     if user.has_perm("products.delete_product"):
        #         return True
        #     if user.has_perm("products.view_product"):
        #         return True
        #     return False
        #
        # return False

    # def has_object_permission(self, request, view, obj):
    #     return True