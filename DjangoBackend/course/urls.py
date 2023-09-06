from django.urls import include, path
from .views import CourseListCreateView,CourseListView,CourseListUpdateView,CourseListDeleteView,getSingleCourse,getInstructorsCourse,courseByCategory
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'courses',getSingleCourse)


urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/create/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/update', CourseListUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete', CourseListDeleteView.as_view(), name='course-delete'),

    path('courses/get_instructor_course/<int:instruc_id>',getInstructorsCourse,name='instruc-courses'),
    path('',include(router.urls)),
    path('courses/get_category_course/<int:cat_id>',courseByCategory,name='category-courses')

]