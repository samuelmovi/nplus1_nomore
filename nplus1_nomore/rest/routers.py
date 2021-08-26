from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# TODO: only accesible by admins
router.register("grandparent-list-bad", views.GrandParentListBad, basename="grandparent-list-bad")
router.register("grandparent-list-good", views.GrandParentListGood, basename="grandparent-list-good")

router.register("parent-list-worst", views.ParentListWorst, basename="parent-list-worst")
router.register("parent-list-bad", views.ParentListBad, basename="parent-list-bad")
router.register("parent-list-good", views.ParentListGood, basename="parent-list-good")

router.register("child-list-bad", views.ChildListBad, basename="child-list-bad")
router.register("child-list-good", views.ChildListGood, basename="child-list-good")
