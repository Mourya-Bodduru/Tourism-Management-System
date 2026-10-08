from django.urls import path
from django.contrib.auth import views as auth_views
from myviews.home import home
from myviews.intro import intro
from myviews.admin_login import admin_login,admin_logout,admin_dashboard
from myviews.sign_in import sign_in ,book_now,cancel,user_dashboard,bookings
from myviews.sign_up import sign_up
from myviews.about import about
from myviews.tour_package import tour_package
from myviews.enquiry import enquiry
from myviews.contact_us import contact_us
from myviews.manage_users import manage_users,approve_todo,approve,delete
from myviews.create_package import packages,create_package
from myviews.admin_enquiry import admin_enquiry,send_reply_email
from myviews.manage_package import manage_package,update_package,delete_package
from myviews.admin_raisedticket import admin_raisedticket,send_reply_email_ticket
from myviews.user_tourpackage import user_tourpackage
from myviews.my_tourhistory import history,cancel_booking
from myviews.raised_ticket import raised_ticket,ticket_raised
from myviews.details import details
from myviews.thank_you import thank_you
from myviews.logout import logout_user
urlpatterns = [  
    path('',intro,name='intro'), 
    path('home/',home,name='home'),
    path('admin_login/',admin_login,name='admin_login'),
    path('sign_in/',sign_in,name='sign_in'), 
    path('sign_up/',sign_up,name='sign_up'),
    path('about/',about,name='about'),
    path('tour_package/',tour_package,name='tour_package'),
    path('enquiry/',enquiry,name='enquiry'),
    path('contact_us/',contact_us,name='contact_us'),
    path('admin_dashboard/',admin_dashboard,name='admin_dashboard'),
    path('manage_users/',manage_users,name='manage_users'),
    path('packages/',packages,name='packages'),
    path('create_package/',create_package,name='create_package'),
    path('admin_enquiry/',admin_enquiry,name='admin_enquiry'),
    path('manage_package/',manage_package,name='manage_package'),  
    path('admin_raisedticket/',admin_raisedticket,name='admin_raisedticket'),
    path('user_dashboard/',user_dashboard,name='user_dashboard'),
    path('user_tourpackage/',user_tourpackage,name='user_tourpackage'),
    path('ticket_raised',ticket_raised,name='ticket_raised'),
    path('raised_ticket/',raised_ticket,name='raised_ticket'),
    path('approve_todo/',approve_todo,name='approve_todo'),
    path('approve/<int:registration_id>/',approve,name='approve'),
    path('delete/<int:registration_id>/',delete,name='delete'),
    path('send_reply_email/<int:pk>/',send_reply_email,name='send_reply_email'),
    path('send_reply_email_ticket/<int:pk>/',send_reply_email_ticket,name='send_reply_email_ticket'),
    path('update_package/<str:pk>/',update_package,name='update_package'),
    path('manage_package/delete_package/<int:id>/',delete_package,name='delete_package'),
    path('details/<int:pk>/',details,name='details'),
    path('history/',history,name='history'),
    path('book_now/<package_id>/', book_now, name='book_now'),
    path('thank_you/',thank_you,name='thank_you'),
    path('cancel/<int:pk>/',cancel,name='cancel'),
    path('cancel_booking/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    path('logout_user/',logout_user,name='logout_user'),
    path('bookings',bookings,name='bookings'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin_logout',admin_logout,name='admin_logout'),
    ]