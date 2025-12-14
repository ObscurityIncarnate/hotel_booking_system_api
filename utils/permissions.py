from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStaff(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff) or bool(obj.reservedBy == request.user.id )
  
class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)  