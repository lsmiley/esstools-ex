


    $(document).ready(function () {
    
      /* Functions */
    
      var loadForm = function () {
        
        var btn = $(this);
        $.ajax({
          url: btn.attr("data-url"),
        
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
    
            $("#modal-orderitem .modal-content").html("");//optional--html() return innerHtml of selected elements
            $("#modal-orderitem").modal("show");
          },
          success: function (data) {
            
            $("#modal-orderitem .modal-content").html(data.html_form);//model-orderitem and model content is in index.html below tabel which will show form pop up
            
          }
        });
      };
    
      var saveForm = function () {
        var form = $(this);
        console.log(form.serialize())
        $.ajax({
          headers: {'X-CSRFToken': csrftoken},
          url: form.attr("action"),//sending request to this url by passing form input data
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          // async : 'false',
          // dataType: "script",
         
      
        
          success : function (data) {//this is the response after data is save to database

            if (data.form_is_valid) {//means if data['form_is_valid'] = True in views.py
            
            alert("successful")
            // console.log(data.html_orderitem_list)
            
             $("#modal-orderitem .close").click();// Close the modal form
         
             

             $("#orderitem-table tbody").html('').append(jQuery.parseHTML(data.html_orderitem_list));
             
            // html('').append(jQuery.parseHTML(data, document, true));
            // <-- Replace the table body 
              //Goto id="orderitem-table"  tbody and then pass data in tbody contain in data.html_orderitem_list
           
            //  $("#modal-orderitem").modal('hide');//--similar but differ in some version
            }

            else {// data['form_is_valid'] = False
            //if false then show the same form with respective warning
              
              $("#modal-orderitem .modal-content").html(data.html_form);//$("#server-results").html(response);
            }
            
          }
        });
        return false;
      };
    
    
      $(".js-orderitem-create").click(loadForm);
      $("#modal-orderitem").on("submit", ".js-orderitem-create-form", saveForm);
    
      
      $("#orderitem-table").on("click", ".js-orderitem-update", loadForm);
      $("#modal-orderitem").on("submit", ".js-orderitem-update-form", saveForm);
    
    
      $("#orderitem-table").on("click", ".js-orderitem-delete", loadForm);
      $("#modal-orderitem").on("submit", ".js-orderitem-delete-form", saveForm);
    
    });
    
    getCookie = (name) => {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
  const csrftoken = getCookie('csrftoken');
 