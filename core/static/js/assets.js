$(document).ready(function () {
    $('#assets').DataTable({
        "language": {
            "url": "http://cdn.datatables.net/plug-ins/1.10.21/i18n/Portuguese-Brasil.json"
        },
        "ajax": "/ativos/listar/json",
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
                "render": function (data) {
                    return "<a href='/ativo/alterar/" + data + "' class='btn btn-icon btn-pill btn-primary btn-sm' data-toggle='tooltip' title='Alterar'><i class='fa fa-fw fa-edit'></i></a><a href='/ativo/alterar/" + data + "' class='btn btn-icon btn-pill btn-danger btn-sm' data-toggle='tooltip' title='Remover'><i class='fa fa-fw fa-trash'></i></a>";
                }
            }
        ]
    });
});