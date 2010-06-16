import views
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # base
    (r'^about/login-required/$', views.DecoratedAboutView),

    # DetailView
    (r'^detail/obj/$',                            views.ObjectDetail),
    url(r'^detail/author/(?P<pk>\d+)/$',          views.AuthorDetail, name="author_detail"),
    (r'^detail/author/byslug/(?P<slug>[\w-]+)/$', views.AuthorDetail),
    (r'^detail/author/invalid/url/$',             views.AuthorDetail),
    (r'^detail/author/invalid/qs/$',              views.AuthorDetail),

    # # EditView
    #     (r'^edit/authors/create/$',                   views.AuthorCreate),
    #     (r'^edit/authors/create/restricted/$',        views.AuthorCreateRestricted),
    #     (r'^edit/author/(?P<pk>\d+)/update/$',        views.AuthorUpdate),
    #     (r'^edit/author/(?P<pk>\d+)/delete/$',        views.AuthorDelete),
    #
    #     # ArchiveView
    #     (r'^dates/books/$',         views.BookArchive),
    #     (r'^dates/books/invalid/$', views.BookArchive),
    #
    #     # ListView
    #     (r'^list/dict/$',                            views.DictList),
    #     url(r'^list/authors/$',                      views.AuthorList, name="authors_list"),
    #     (r'^list/authors/paginated/$',               views.AuthorList),
    #     (r'^list/authors/paginated/(?P<page>\d+)/$', views.AuthorList),
    #     (r'^list/authors/notempty/$',                views.AuthorList),
    #     (r'^list/authors/template_object_name/$',    views.AuthorList),
    #     (r'^list/authors/invalid/$',                 views.AuthorList),
    #
    #     # YearView
    #     # Mixing keyword and possitional captures below is intentional; the views
    #     # ought to be able to accept either.
    #     (r'^dates/books/(?P<year>\d{4})/$',          views.BookYearArchive),
    #     (r'^dates/books/(\d{4})/make_object_list/$', views.BookYearArchive),
    #     (r'^dates/books/(\d{4})/allow_empty/$',      views.BookYearArchive),
    #     (r'^dates/books/(\d{4})/allow_future/$',     views.BookYearArchive),
    #     (r'^dates/books/no_year/$',                  views.BookYearArchive),
    #
    #     # MonthView
    #     (r'^dates/books/(\d{4})/([a-z]{3})/$',              views.BookMonthArchive),
    #     (r'^dates/books/(\d{4})/(\d{1,2})/$',               views.BookMonthArchive),
    #     (r'^dates/books/(\d{4})/([a-z]{3})/allow_empty/$',  views.BookMonthArchive),
    #     (r'^dates/books/(\d{4})/([a-z]{3})/allow_future/$', views.BookMonthArchive),
    #     (r'^dates/books/(\d{4})/no_month/$',                views.BookMonthArchive),
    #
    #     # WeekView
    #     (r'^dates/books/(\d{4})/week/(\d{1,2})/$',              views.BookWeekArchive),
    #     (r'^dates/books/(\d{4})/week/(\d{1,2})/allow_empty/$',  views.BookWeekArchive),
    #     (r'^dates/books/(\d{4})/week/(\d{1,2})/allow_future/$', views.BookWeekArchive),
    #     (r'^dates/books/(\d{4})/week/no_week/$',                views.BookWeekArchive),
    #
    #     # DayView
    #     (r'^dates/books/(\d{4})/([a-z]{3})/(\d{1,2})/$',              views.BookDayArchive),
    #     (r'^dates/books/(\d{4})/(\d{1,2})/(\d{1,2})/$',               views.BookDayArchive),
    #     (r'^dates/books/(\d{4})/([a-z]{3})/(\d{1,2})/allow_empty/$',  views.BookDayArchive),
    #     (r'^dates/books/(\d{4})/([a-z]{3})/(\d{1,2})/allow_future/$', views.BookDayArchive),
    #     (r'^dates/books/(\d{4})/([a-z]{3})/no_day/$',                 views.BookDayArchive),
    #
    #     # TodayView
    #     (r'dates/books/today/$',              views.BookTodayArchive),
    #     (r'dates/books/today/allow_empty/$',  views.BookTodayArchive),
    #
    #     # DateDetailView
    #     (r'^dates/books/(\d{4})/([a-z]{3})/(\d{1,2})/(\d+)/$',              views.BookDetail),
    #     (r'^dates/books/(\d{4})/(\d{1,2})/(\d{1,2})/(\d+)/$',               views.BookDetail),
    #     (r'^dates/books/(\d{4})/([a-z]{3})/(\d{1,2})/(\d+)/allow_future/$', views.BookDetail),
    #     (r'^dates/books/(\d{4})/([a-z]{3})/(\d{1,2})/nopk/$',               views.BookDetail),
    #
    #     (r'^dates/books/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/byslug/(?P<slug>[\w-]+)/$', views.BookDetail),

    # Useful for testing redirects
    (r'^accounts/login/$',  'django.contrib.auth.views.login')
)
