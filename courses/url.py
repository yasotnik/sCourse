from django.conf.urls import url
from . import views


app_name = 'courses'


urlpatterns = [
    # URL for course list /courses
    url(r'^$', views.CoursesView.as_view(), name='index'),

    # URL for course list /courses
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # URL for exact course /course/id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='course_info'),

    # /courses/add
    url(r'add/$', views.CourseCreate.as_view(), name='add_course'),

    # /courses/course/add_lecture
    url(r'add_lecture/$', views.LectureCreate.as_view(), name='add_lecture'),

    # URL for update course
    url(r'update/(?P<pk>[0-9]+)/$', views.CourseUpdate.as_view(), name='course_update'),

    # /courses/id/delete
    url(r'(?P<pk>[0-9]+)/delete/$', views.CourseDelete.as_view(), name='course_delete'),

]
