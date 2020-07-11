
function getData(filter, _callback) {
    return $('#assets').DataTable({
        "ajax": {
            "url": "/equipamentos/listar/json",
            "type": "POST",
            "data": {
                "localizacao": function() { return $('#unidade').val() },
                "setor": function() { return $('#setor').val() },
                "grupo": function() { return $('#localizacao').val() },
                "categoria": function() { return $('#equipamento').val() },
                "status": function() { return $('#status').val() },
                "csrfmiddlewaretoken": function() { return $("input[name='csrfmiddlewaretoken']").val() },
            }
        },
        responsive: true,
        "bLengthChange": false,
        columnDefs: [
            { responsivePriority: 1, targets: 0 },
            { responsivePriority: 2, targets: -1 }
        ],
        "language": {
            "url": "http://cdn.datatables.net/plug-ins/1.10.21/i18n/Portuguese-Brasil.json"
        },
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
                "render": function (data, ) {
                    result = "<a href='/equipamento/editar/" + data + "' class='btn btn-icon btn-pill btn-primary btn-sm' data-toggle='tooltip' title='Editar'><i class='fa fa-fw fa-edit'></i> </a> <a href='/equipamento/remover/" + data + "' class='btn btn-icon btn-pill btn-danger btn-sm' data-toggle='tooltip' title='Remover'> <i class='fa fa-fw fa-trash'></i></a>";
                    return result
                }
            }
        ]
    });
    _callback();
}