$("#drawer").bind "show.bs.drawer", () ->
    $("#drawer .fa-chevron-right").hide()
    $("#drawer .fa-chevron-left").show()

$("#drawer").bind "hide.bs.drawer", () ->
    $("#drawer .fa-chevron-right").show()
    $("#drawer .fa-chevron-left").hide()

fix_size = () ->
    height = $(window).height() - $(".navbar").height() - $(".footer").height()
    console.log height
    $(".has-inner-drawer").height height

do fix_size
$(window).resize fix_size
