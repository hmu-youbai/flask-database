$(document).ready(function() {
    $('#idValue').on('input', function() {
        var input_type = $('#idType').val(); 
        var input = $(this).val();
        if (input.length > 0) {
            $.ajax({
                url: '/suggest-genes',
                type: 'GET',
                data: { query: input, query_type: input_type },
                success: function(data) {
                    var suggestions = $('#geneSuggestions');
                    suggestions.empty().show();
                    data.forEach(function(item) {
                        $('<div class="list-group-item list-group-item-action">').text(item)
                            .appendTo(suggestions)
                            .on('click', function() {
                                $('#idValue').val($(this).text());
                                suggestions.hide();
                            });
                    });
                }
            });
        } else {
            $('#geneSuggestions').hide();
        }
    });

    // 监听输入框获得焦点事件
    $('#idValue').on('focus', function() {
        var input = $(this).val();
        var suggestions = $('#geneSuggestions');
        if (input.length > 0 && suggestions.children().length > 0) {
            suggestions.show();
        }
    });

    // 监听文档的点击事件，检查点击是否发生在提示框或输入框外
    $(document).on('click', function(e) {
        if (!$(e.target).closest('#idValue, #geneSuggestions').length) {
            $('#geneSuggestions').hide(); // 如果点击区域不包括输入框和提示框，则隐藏提示框
        }
    });

    $('#goButton').click(function() {
        var idType = $('#idType').val();
        var idValue = $('#idValue').val();
        $.ajax({
            url: '/fetch-data',
            type: 'POST',
            data: {
                idType: idType,
                idValue: idValue
            },
            success: function(response) { 
	    $('#genecard').html( `
                    <h2>${response.genename}</h2>
                    <p><strong>Full name:</strong> ${response.full_name} </p>
                    <p><strong>Aliases:</strong> ${response.aliases}</p>
                    <p><strong>Location:</strong> ${response.location}</p>
                    <p><strong>Description:</strong> ${response.description}</p>
                    <p><strong>Links:</strong> 
                        <a href="${response.genecards}">Genecard</a>,
                        <a href="${response.ncbi}">NCBI</a>,
                        <a href="${response.ensembl}">Ensembl</a>,
                        <a href="${response.wikigenes}">Wikigenes</a>
                    </p>`);
            $('#featurePlotResult').html(`
                <div class="image-row">
                    <div class="image-container">
                        <img src="${response.featurePlot}" alt="Feature Plot" />
                    </div>
                    <div class="image-container">
                        <img src="${response.featurePlot2}" alt="Violin Plot" />
                    </div>
                </div>
	        <div class="annotation-container">
                    <p class="plot-annotation">(Left: UMAP; Right: t-SNE)</p>
                </div>
            `);
                $('#violinPlotResult').html(`<img src="${response.violinPlot}" alt="violin Plot" />`);

            $('#developmentalStagesResult').html(`
                <div class="image-row">
                    <div class="image-container">
                        <img src="${response.developmentalStages}" alt="Feature Plot" />
                    </div>
                    <div class="image-container">
                        <img src="${response.cellTypeResult}" alt="Violin Plot" />
                    </div>
                </div>
                <div class="annotation-container">
                    <p class="plot-annotation">(Left: developmental stage; Right: cell type)</p>
                </div>

            `);

               
            },
            error: function() {
                alert('Error fetching data');
            }
        });
    });
});

