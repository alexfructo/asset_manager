$(document).ready(function () {
    $('#assets').DataTable({
        responsive: true,
        dom: 'l<"toolbar">frtip',
        initComplete: function () {
            $("div.toolbar").html("<button href='#' class='btn btn-success'>Cadastrar</button>");
        },
        "bLengthChange": false,
        columnDefs: [
            { responsivePriority: 1, targets: 0 },
            { responsivePriority: 2, targets: -1 }
        ],
        "language": {
            "url": "http://cdn.datatables.net/plug-ins/1.10.21/i18n/Portuguese-Brasil.json"
        },
        "ajax": "/equipamentos/listar/json",
        "columns": [
            { "data": "localizacao" },
            { "data": "setor" },
            { "data": "grupo" },
            { "data": "categoria" },
            { "data": "fabricante" },
            { "data": "modelo" },
            { "data": "numero_serie" },
            { "data": "numero_patrimonio" },
            { "data": "status" },
            {
                "data": "codigo",
                "render": function (data,) {
                    result = "<a href='/equipamento/visualizar/" + data + "' class='btn btn-icon btn-pill btn-primary btn-sm' data-toggle='tooltip' title='Alterar'><i class='fa fa-fw fa-edit'></i> </a> <a href='/equipamento/remover/" + data + "' class='btn btn-icon btn-pill btn-danger btn-sm' data-toggle='tooltip' title='Remover'> <i class='fa fa-fw fa-trash'></i></a>";
                    return result
                }
            }
        ]
    });
}); 