from rest_framework import permissions

class IsStaffEditoPermissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.user.is_staff():
            return False
        return super().has_permission(request, view)
    def has_permission(self, request, view):#app_name.verb_model_name
        user=request.user
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm("product.add_product"):
                return True
            if user.has_perm("product.change_product"):
                return True
            if user.has_perm("product.delete_product"):
                return True
            if user.has_perm("product.view_product"):
                return True
            return False

        return False

    # def has_object_permission(self, request, view, obj):
    #     return True