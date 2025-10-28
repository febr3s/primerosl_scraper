Spotlight.onLoad(function(){
  $('.zpr-link').on('click', function() {
    var modalDialog = $('#blacklight-modal .modal-dialog');
    var modalContent = modalDialog.find('.modal-content')
    modalDialog.removeClass('modal-lg')
    modalDialog.addClass('modal-xl')
    modalContent.html('<div id="osd-modal-container"></div>');
    var controls = [
      '<div class="controls d-flex justify-content-center justify-content-md-end">',
      '  <div class="custom-close-controls pr-3 pt-3">',
      '    <button type="button" class="btn btn-dark" data-dismiss="modal" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41z"/></svg></button>',
      '  </div>',
      '  <div class="zoom-controls mb-3 mr-md-3">',
      '    <button id="osd-zoom-in" type="button" class="btn btn-dark"><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14zm.5-7H9v2H7v1h2v2h1v-2h2V9h-2z"/></svg></button>',
      '    <button id="osd-zoom-out" type="button" class="btn btn-dark"><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14zM7 9h5v1H7V9z"/></svg></button>',
      '  </div>',
      '  <div id="empty-div-required-by-osd"></div>',
      '</div>'
    ].join("\n");


    $('#osd-modal-container').append('<div id="osd-div"></div>');
    $('#osd-modal-container').append(controls);

    $('#blacklight-modal').modal('show');
    
    $('#blacklight-modal').one('hidden.bs.modal', function (event) {
      modalDialog.removeClass('modal-xl')
      modalDialog.addClass('modal-lg')
    });

    OpenSeadragon({
      id: 'osd-div',
      zoomInButton: "osd-zoom-in",
      zoomOutButton: "osd-zoom-out",
      // This is a hack where OpenSeadragon (if using mapped buttons) requires you
      // to map all of the buttons.
      homeButton: "empty-div-required-by-osd",
      fullPageButton: "empty-div-required-by-osd",
      nextButton: "empty-div-required-by-osd",
      previousButton: "empty-div-required-by-osd",
      tileSources: [$(this).data('iiif-tilesource')]
    })
  });
});
