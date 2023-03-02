from rest_framework.permissions import BasePermission

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return False

        # Check if user is a customer
        if not request.user.is_customer:
            return False
        
        return True


class IsSupplier(BasePermission):
    def has_permission(self, request, view):

        # Check if user is authenticated
        if not request.user.is_authenticated:
            return False

        # Check if user is a supplier
        if not request.user.is_supplier:
            return False

        return True