
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
        var errors = false, reqOnceErrors = false;
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
        var reqOneFields = form.find('.required-one');
        if(reqOneFields.length) { reqOnceErrors = true; }
        reqOneFields.each(function(){
          var field = $(this);
          if($.trim(field.val())) {
            reqOnceErrors = false;
          }
        });
        if(reqOnceErrors) {
          errors = true;
          reqOneFields.addClass('error');
          reqOneFields.filter(':last').before('<div class="error-message"><i class="fontello icon-up-bold"></i>Одно из полей должно быть обязательно заполнено</div>');
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
    auto: true,
    minSlides: 3,
    maxSlides: 3,
    adaptiveHeight: true,
    onSliderLoad: function(currentIndex){
      //console.log(currentIndex);
    },
    onSlideBefore: function(slideElement, oldIndex, newIndex){
      //console.log(slideElement);
      var elems = slideElement.parent().find('li'), cloneElem = slideElement, lastIndex = (elems.filter(':not(.bx-clone)').length - 1);
      if(newIndex == 0 && oldIndex == lastIndex) {
        cloneElem = elems.filter(':not(.bx-clone):eq(' + oldIndex + ')').next();
      } else if(newIndex == lastIndex && oldIndex == 0) {
        cloneElem = elems.filter(':not(.bx-clone):eq(' + oldIndex + ')').prev();
      }
      elems.removeClass('faded');
      elems.not(slideElement).not(cloneElem).addClass('faded');
    },
    onSlideAfter: function(slideElement, oldIndex, newIndex){
      slideElement.removeClass('faded');
    }
  });

  var datePickElem = $('.block-events #date-filter');
  if(datePickElem) {

    datePickElem.each(function(){
      var loc = {
        days: ['воскресенье','понедельник','вторник','среда','четверг','пятница','суббота'],
        daysShort: ['Вс','Пн','Вт','Ср','Чт','Пт','Сб'],
        daysMin: ['Вс','Пн','Вт','Ср','Чт','Пт','Сб'],
        months: ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'],
        monthsShort:  ['Янв','Фев','Мар','Апр','Май','Июн','Июл','Авг','Сен','Окт','Ноя','Дек'],
        weekMin:  'нд'
      };
      var form = datePickElem.parents('form:first'), fromField = form.find('.date_from'), toField = form.find('.date_to'), d = new Date(),
          fromDate = fromField.val() ? fromField.val() : '', toDate = toField.val() ? toField.val() : '';
      if (d.getMonth() == 11) {
          var current = new Date(d.getFullYear() + 1, 0, 1);
      } else {
          var current = new Date(d.getFullYear(), d.getMonth() + 1, 1);
      }
      datePickElem.DatePicker({
        flat: true,
        format: 'Y-m-d',
        date: [fromDate,toDate],
        current: current,
        calendars: 2,
        mode: 'range',
        starts: 1,
        locale: loc,
        onChange: function(formated, dates){
          var datesArr = formated.splice(',');
          fromField.val(datesArr[0]);
          toField.val(datesArr[1]);
          //if ($('#closeOnSelect input').attr('checked')) {
          //  $('#inputDate').DatePickerHide();
          //}
        }
      });
    });
  }
  var eventsBlock = $('.block-events-filters');
  if(eventsBlock.length) {
    var eventsFiltersForm = eventsBlock.find('form'), eventsFilterTypeSel = eventsFiltersForm.find('.filter-type-select'), eventsFilterTypeBtns = eventsBlock.find('.filters li a');
    $('.block-events-filters .filters li a').click(function(e){
      e.preventDefault();
      var btn = $(this), btns = btn.parents('ul').find('[data-typeval]'), val = btn.data('typeval');
      if(btn.parent().hasClass('active')) {
        btns.parent().removeClass('active');
        eventsFilterTypeSel.val('').change();
      } else {
        btns.not(btn).parent().removeClass('active');
        eventsFilterTypeSel.val(val).change();
        btn.parent().addClass('active');
      }
    });
    if(eventsFilterTypeSel.val()) {
      eventsFilterTypeBtns.filter('[data-typeval="' + eventsFilterTypeSel.val() + '"]').parent().addClass('active');
    }
  }

  $('.ripple-me, .toggle-bars').ripples();

  $('.ajaxify-form').ajaxifyForm();

});

$(document).on('click', '.block-icons-bar .toggle-bars', function(e){
  e.preventDefault();
  $(this).parent().toggleClass('showed');
});

$(document).on('click', '.block-sights-filters .btn-filter', function(e){
  //e.preventDefault();
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

$(window).on('resize load', function(){
  var rows = $('.block-food-rows .food-rows'), inRow = 4, resolutionName = $('.visible-detect div').filter(':visible').data('resolution');
  if(resolutionName == 'xs' || resolutionName == 'sm') inRow = 2;
  rows.each(function(){
    var cells = $(this).find('.food-row'), i = 1, maxH = 0;
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

$(window).on('resize load', function(){
  var windowWidth = $(window).width(), slider = $('.block-slider-promo'), sliderView = slider.find('.bx-viewport'), sliderWidth = sliderView.width(),
      tgWidth = ((windowWidth - sliderWidth)/2 + 15), controls = slider.find('.bx-controls-direction a');
  if(tgWidth > 0) {
    controls.css({width: tgWidth + 'px'});
  }
});


$(window).on('resize load', function(){
  var rows = $('.block-museum-rows .museum-rows'), inRow = 4, resolutionName = $('.visible-detect div').filter(':visible').data('resolution');
  if(resolutionName == 'xs' || resolutionName == 'sm') inRow = 2;
  rows.each(function(){
    var cells = $(this).find('.museum-row'), i = 1, maxH = 0;
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

//
//$(window).on('resize load', function(){
//  var rows = $('.block-food-rows .food-rows'), inRow = 4, resolutionName = $('.visible-detect div').filter(':visible').data('resolution');
//  if(resolutionName == 'xs' || resolutionName == 'sm') inRow = 2;
//  rows.each(function(){
//    var cells = $(this).find('.food-row'), i = 1, maxH = 0;
//    cells.css({'min-height': 0});
//    cells.each(function(){
//      var cell = $(this), h = cell.outerHeight();
//      cell.css({'min-height': 0}).addClass('not-done');
//      if(h > maxH) maxH = h;
//      if(i >= inRow) {
//        cells.filter('.not-done').css({'min-height': maxH}).removeClass('not-done');
//        maxH = 0;
//        i = 1;
//      } else {
//        i++;
//      }
//    });
//  });
//}).resize();
//
//
//$(window).on('resize load', function(){
//  var rows = $('.block-food-rows .food-rows'), inRow = 4, resolutionName = $('.visible-detect div').filter(':visible').data('resolution');
//  if(resolutionName == 'xs' || resolutionName == 'sm') inRow = 2;
//  rows.each(function(){
//    var cells = $(this).find('.food-row'), i = 1, maxH = 0;
//    cells.css({'min-height': 0});
//    cells.each(function(){
//      var cell = $(this), h = cell.outerHeight();
//      cell.css({'min-height': 0}).addClass('not-done');
//      if(h > maxH) maxH = h;
//      if(i >= inRow) {
//        cells.filter('.not-done').css({'min-height': maxH}).removeClass('not-done');
//        maxH = 0;
//        i = 1;
//      } else {
//        i++;
//      }
//    });
//  });
//}).resize();
