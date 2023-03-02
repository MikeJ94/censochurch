
$(document).ready(function() {
   $('#bootstrapdatatable').DataTable( {
      colReorder: true,
      responsive: true,
      /* dom: 'Blfrtip', */ 
      dom: 'Bfrtip',
      aLengthMenu: [[3, 5, 10, 25, -1], [3, 5, 10, 25, "Mostrar todo"]],
      iDisplayLength: 3,
      /*fieldSeparator: '\t',*/

        buttons: [

            {
                extend:'copyHtml5',
                text:'<i class="bi bi-clipboard"></i>Copiar',
                titleAttr: 'Copiar'
            },


            {
                extend:'print',
                text:'<i class="bi bi-printer"></i>Print',
                titleAttr: 'Imprimir'

            },

            {
                extend: 'pdfHtml5',
                text:  '<i class="bi bi-filetype-pdf"></i>PDF',
                titleAttr: 'PDF',
                orientation: 'landscape',
                pageSize: 'LEGAL',
                download: 'open',
                title: 'Listado de Miembros'
            },

            {
                extend: 'excelHtml5',
                text:  '<i class="bi bi-file-earmark-spreadsheet"></i>Excel',
                titleAttr: 'Excel',
                autoFilter: true,
                sheetName: 'Listado de Miembros',
                title: 'Listado de Miembros',
                /* exportOptions: {
                    columns: [ 1, 2 ]
                }, */

            },

            {
                extend: 'csvHtml5',
                text:  '<i class="bi bi-filetype-csv"></i>CSV',
                titleAttr: 'CSV'
            },

            {
                extend:    'pageLength',
                text:  '<i class="bi bi-plus-circle"></i>Ver',
                titleAttr: 'Registros a mostrar',
                className: 'selectTable'
            },
        
        ]
   

   } );


} );


