jQuery('document').ready(function() {
// jQuery('header').remove();

// 
// var cat1, cat2;
// cat1=123;
// cat2=23;
// alert(cat1+cat2);
 
//   var a1, a2;
//   a1=144^2;
//   a2=a1-100^2;
//   alert (a1+a2);
jQuery('button').on('click', function() {
 var value1, value2, value3;
 value1 = jQuery('#val1').val();
 value2 = jQuery('#val2').val();

 value1 = parseInt(value1);
 value2 = parseInt(value2);

 value3 = value1 + value2;

 alert(value3);
});
})