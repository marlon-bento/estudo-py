from rest_framework import permissions


class IsLibrarian(permissions.BasePermission):
    
    # checando um objeto em si
    def has_object_permission(self, request, view, obj):
        return obj.borrower == request.user
    
    #checando coisas aleatorias
    def has_permission(self, request, view):
        return super().has_permission(request, view)