
var ajaxifyCallbacks = function () {
  return {
    //Submit callbacks
    submit: {
      //Default submit callback
      defaultCallback: function(e, form, data) {
        
      },
      orderACallCallback: function(e, form, data) {
        form.prepend('<div class="status-message"><i class="mdi-alert-error"></i>Спасибо. Ожидайте звонка.</div>');
        form[0].reset();
        form.find('.form-control').addClass('empty');
        setTimeout(function(){ form.parents('.modal').modal('hide'); form.find('.status-message').remove(); }, 3000);
      },
      orderExcursionCallback: function(e, form, data) {
        form.prepend('<div class="status-message"><i class="mdi-alert-error"></i>Спасибо. Ожидайте звонка.</div>');
        form[0].reset();
        form.find('.form-control').addClass('empty');
        setTimeout(function(){ form.parents('.modal').modal('hide'); form.find('.status-message').remove(); }, 3000);
      }
    },
    //Validate callbacks
    validate: {
      //Default validate callback. Return TRUE if there is some errors
      defaultCallback: function(e, form, formData) {
        form.find('.error').removeClass('error');
        form.find('.error-message').remove();
        return false;
      },
      orderACallCallback: function(e, form, formData) {
        var errors = false;
        form.find('.error').removeClass('error');
        form.find('.error-message').remove();
        form.find('.required').each(function(){
          var field = $(this);
          if(!$.trim(field.val())) {
            field.before('<div class="error-message"><i class="fontello icon-up-bold"></i>Это обязательное поле</div>');
            field.addClass('error');
            errors = true;
          } else if(field.attr('type') == 'checkbox' && !field.is(':checked')) {
            field.parent().before('<div class="error-message">Это обязательное поле</div>');
            errors = true;
          }
        });
        var dreq = 0;
        form.find('.dreq').each(function(){
          var field = $(this);
          if($.trim(field.val())) {
            dreq = dreq + 1;
          } else if(field.attr('type') == 'checkbox' && field.is(':checked')) {
            dreq = dreq + 1;
          }
        });

          if(dreq < 1) {
            form.find('.dreq1').before('<div class="error-message"><i></i>Одно из полей должно быть обязательно заполнено</div>');
            form.find('.dreq1').addClass('error');
            form.find('.dreq').addClass('error');
            errors = true;
          }
        return errors;
      },
      orderExcursionCallback: function(e, form, formData) {
        var errors = false;
        form.find('.error').removeClass('error');
        form.find('.error-message').remove();
        form.find('.required').each(function(){
          var field = $(this);
          if(!$.trim(field.val())) {
            field.before('<div class="error-message"><i class="fontello icon-up-bold"></i>Это обязательное поле</div>');
            field.addClass('error');
            errors = true;
          } else if(field.attr('type') == 'checkbox' && !field.is(':checked')) {
            field.parent().before('<div class="error-message">Это обязательное поле</div>');
            errors = true;
          }
        });
        return errors;
      }
    }
  };
}();

$.extend($.fn, {
  //Good serialization of form for AJAX
  serializeFormToObject: function(){
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
      if (o[this.name] !== undefined) {
        if (!o[this.name].push) {
            o[this.name] = [o[this.name]];
        }
        o[this.name].push(this.value || '');
      } else {
        o[this.name] = this.value || '';
      }
    });
    return o;
  },
  //AJAX Form
  ajaxifyForm: function(){
    $(this).each(function(){
      var form = $(this);
      form.submit(function(e) {
        e.preventDefault();
        var submitCallback = form.data("submit") && $.isFunction(ajaxifyCallbacks.submit[form.data("submit")]) ? ajaxifyCallbacks.submit[form.data("submit")] : ajaxifyCallbacks.submit.defaultCallback,
            validateCallback = form.data("validate") && $.isFunction(ajaxifyCallbacks.validate[form.data("validate")]) ? ajaxifyCallbacks.validate[form.data("validate")] : ajaxifyCallbacks.validate.defaultCallback,
            method = form.attr('method') ? form.attr('method').toLowerCase() : 'get',
            errors = false, formData = (method == 'post') ? new FormData(form[0]) : form.serializeFormToObject(),
            url = form.attr('action') ?  form.attr('action') : window.location.href;
        //Check form for errors
        errors = validateCallback(e, form, formData);
        //If NO ERRORS than SEND form
        if(!errors) {
          $.ajax({
            url: url,
            data: formData,
            method: method,
            headers: {'X-Requested-With': 'XMLHttpRequest'},
            processData: method == 'post' ? false : true,
            contentType: method == 'post' ? false : true,
            success: function(data) {
              //Trigger submit callback
              submitCallback(e, form, data);
            }
          });
        }
      });
    });
    
    return this;
  }
  
});



$(document).ready(function(){
  
  $('.bxslider').bxSlider({
    onSliderLoad: function(){
      $('.bxslider li a').ripples();
    },
  });
  
  $('.toggle-bars').ripples();
  
  $('.ajaxify-form').ajaxifyForm();
  
});

$(document).on('click', '.block-icons-bar .toggle-bars', function(e){
  e.preventDefault();
  $(this).parent().toggleClass('showed');
});

$(document).on('click', '.block-sights-filters .btn-filter', function(e){
  e.preventDefault();
  var btn = $(this);
  btn.removeClass('changed');
  btn.toggleClass('active');
  btn.addClass('changed');
});

$(document).on('click', '.btn-load-more-v1', function(e){
  e.preventDefault();
  var btn = $(this), cont = btn.parents('.block-sights-n-filters').find('.block-sights-rows'), count = cont.find('.sights-row').length, url = btn.data('url');
  btn.addClass('loading');
  $.get(url, {offset: count}, function(data){
    console.log(data);
    btn.removeClass('loading');
    if(data.count) { btn.data('count', data.count); }
    if(data.end) { btn.parent().hide(); }
    if(data.rows) {
      var rows = $(data.rows);
      rows.css({opacity: 0});
      cont.append(rows);
      rows.animate({opacity: 1}, 300, function(){
        rows.find('a').ripples();
        $(window).resize();
      });
    }
  });
});

$(document).on('click', '.to-up-wrap a', function(e){
  e.preventDefault();
  $('html, body').animate({scrollTop: 0}, 1000);
});

$(window).on('resize load', function(){
  var rows = $('.block-sights-rows .sights-rows'), inRow = 4, resolutionName = $('.visible-detect div').filter(':visible').data('resolution');
  if(resolutionName == 'xs' || resolutionName == 'sm') inRow = 2;
  //console.log(resolutionName);
  //console.log(inRow);
  rows.each(function(){
    var cells = $(this).find('.sights-row'), i = 1, maxH = 0;
    cells.css({'min-height': 0});
    cells.each(function(){
      var cell = $(this), h = cell.outerHeight();
      cell.css({'min-height': 0}).addClass('not-done');
      if(h > maxH) maxH = h;
      if(i >= inRow) {
        cells.filter('.not-done').css({'min-height': maxH}).removeClass('not-done');
        maxH = 0;
        i = 1;
      } else {
        i++;
      }
    });
  });
}).resize();

$(window).on('scroll', function(){
  var top = $(window).scrollTop(), iconsBar = $('.block-icons-bar');
  if(top >= 65) {
    iconsBar.addClass('fixed');
  } else {
    iconsBar.find('.left-wrap-inner, .right-wrap-inner').scrollTop(0);
    iconsBar.removeClass('fixed');
  }
}).scroll();