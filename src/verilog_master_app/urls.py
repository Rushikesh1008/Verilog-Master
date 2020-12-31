from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('form_submit', views.form_submit,name="form_submit"),
    path('intro1/',views.intro1,name="intro1"),
    path('intro2/',views.intro2,name="intro2"),
    path('verilog-basics-1/',views.verilogbasics1, name="verilogbasics1"),
    path('digital-basics/',views.digital_basics,name="digital_basics"),
    path('modules-and-port-mappings/',views.modules_and_port_mappings, name="modules_and_port_mappings"),
    path('gate-level-modelling/',views.gate_level_modelling, name="gate_level_modelling"),
    path('behavioral-2/',views.behavioral_2,name="behavioral2"),
    path('half-adder/',views.half_adder,name="half_adder"),
<<<<<<< HEAD
    path('mux/',views.mux,name="mux"),
=======
>>>>>>> ed1cff22d4cc0a4cff09c5474a4b011cf4ed70c6

]
