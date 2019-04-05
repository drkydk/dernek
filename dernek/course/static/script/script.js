/**
 * Created by yilmaz on 22.02.2017.
 */

// use $(document).on(events, selector, data, handler); instead for responsive html insertion

$('#login-link').on('click', function(e){
    e.preventDefault();
    $('.login').fadeToggle('slow');
    $(this).toggleClass('green');
});


$(document).on('click', '#register-link', (function () {
    $('.register').fadeToggle('slow');
    $(this).toggleClass('green');
}));

$(document).on('click', "#main-link", function(e) {
    e.preventDefault();
    location.reload();
});

$(document).on('click', '.clickable_shedule', (function (e) {
    var self = this;
    if ($(self).find('.dummy-div').length == 0) {
        $('.lecture-form').css('display', 'none');
        $(self).find('.lecture-form').css('display', 'inline');
    }
}));

$(document).on('click', '.students-link', (function () {
    var self = this;
    $(self).find('i').fadeToggle()
}));

var lecture_form = $('.lecture-form')
lecture_form.submit(function (e) {
    var self = this;
    e.preventDefault();
    $.ajax({
        url: 'add-lecture',
        type: 'post',
        data: $(self).serialize(),
        success: function (data) {
            alert(data);
            location.reload();
        },
        error: function (data) {
            alert('HATA!')
        }
    });
});

$(document).on('click', '.delete-icon', (function (e) {
    var self = this;
    e.preventDefault();

    $.ajax({
        url: 'delete-lecture',
        type: 'post',
        data: $(self).next('.lecture-delete-form').serialize(),
        success: function (data) {
            alert(data);
            location.reload();
        },
        error: function (data) {
            alert('HATA!')
        }
    });
}));

var login_form = $('#login-form');
login_form.submit(function (e) {
    e.preventDefault();
    $.ajax({
        url: 'login',
        type: 'post',
        data: login_form.serialize(),
        success: function (data) {
            alert(data);
            location.reload();
        },
        error: function (data) {
            alert('HATA!')
        }
    });

});

var hsearch_form = $('#history');
hsearch_form.submit(function (e) {
    e.preventDefault();
    $.ajax({
        url: 'hsearch',
        type: 'post',
        data: hsearch_form.serialize(),
        success: function (data) {
            $('#hsearch_res').empty();
            $('#hsearch_res').append(data);
            $('.history').fadeToggle('fast');
            $('#history-link').removeClass('green');
            $('#wrap-main').hide();
        },
        error: function(data) {
            alert('Hatalı Arama!' + data)
        }
    });
});

$(document).on('click', '#logout-link', (function (e) {
    e.preventDefault();
    $.ajax({
        url: 'logout',
        type: 'post',
        success: function (data) {
            alert(data);
            location.reload();
        },
        error: function (data) {
            alert('HATA!')
        }
    });
}));

var register_form = $('#register-form')
register_form.submit(function (e) {
    e.preventDefault();
    $.ajax({
        url: 'register',
        type: 'post',
        data: register_form.serialize(),
        success: function (data) {
            alert(data);
            location.reload();
        },
        error: function (data) {
            alert('HATA!')
        }
    });
});

$(document).ready(function() {
        $('#useradmin').html('<object data="/admin/auth/user/" style="position:relative;float:left;width:100%;height:800px;">');
        var x = document.getElementsByClassName("sidebar");
        x.style.display = "none";
});

  $( function() {
    $( "#datepicker" ).datepicker({
        dateFormat: "yy-mm-dd"
    });
  } );

    $( function() {
    $( "#datepicker2" ).datepicker({
        dateFormat: "yy-mm-dd"
    });
  } );


$(document).on('mousedown', (function (e) {
    // For login form
    var container_login = $(".login");

    if (!container_login.is(e.target) // if the target of the click isn't the container...
        && container_login.has(e.target).length === 0 // ... nor a descendant of the container
        && !$('#login-link').is(e.target))
    {
        container_login.hide();
        $('#login-link').removeClass('green');
    }

    // For register form
    var container_register = $(".register");

    if (!container_register.is(e.target) // if the target of the click isn't the container...
        && container_register.has(e.target).length === 0 // ... nor a descendant of the container
        && !$('#register-link').is(e.target)) // ... nor the referring link itself
    {
        container_register.hide();
        $('#register-link').removeClass('green');
    }

    // For useradmin form
    var useradmin_form = $("#useradmin");

    if (!useradmin_form.is(e.target)
        && useradmin_form.has(e.target).length === 0
        && !$('#useradmin-link').is(e.target))
    {
        useradmin_form.hide();
        $('#useradmin-link').removeClass('green');
    }

    // For history search form
    var history_form = $(".history");
    var datepicker_field = $("#ui-datepicker-div *");

    if (!history_form.is(e.target)
    && history_form.has(e.target).length === 0
    && !$('#history-link').is(e.target)
    && !datepicker_field.is(e.target))
    {
        history_form.hide();
        $('#history-link').removeClass('green');
    }
}));

$(document).on('click', '#useradmin-link', (function (e) {
    e.preventDefault();
    $('#useradmin').fadeToggle('slow');
    $(this).toggleClass('green');
}));



$(document).on('click', '#history-link', (function (e) {
    e.preventDefault();
    $('.history').fadeToggle('slow');
    $(this).toggleClass('green');
}));

$(window).on('scroll', _.debounce(function() {
   if($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
       // var extCount = $('#extension_counter').length + 1;
       var extCount = $('div.extension_counter').length + 1;
            $.ajax({
                url: 'homepage_extension',
                type: 'post',
                data: {'count': extCount, 'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()},
                success: function (data) {
                    $('#extension').append(data);
                }
                ,
                error: function (data) {
                    alert('Dynamic Page Extension Error!' + data)
                }

       });
   }
}, 200));
