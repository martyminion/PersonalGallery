function showModal(imgname,imgdesc,imgurl,imglocsp,imglocct,imgloccntry,imgcat){
  $("#imgmdtitle").text(imgname)
  $("#ScrollableModal").modal("show")
  $(".modal-title").text(imgname)
  $(".mod-img").attr("src",imgurl)
  $("#imgmddescription").text(imgdesc)
  $("#imgmdlocationspecifc").text("Location: " + imglocsp)
  $("#imgmdlocation").text(imglocct+","+imgloccntry)
  $("#imgmdcategory").text("Category: " + imgcat)
}

function copy(){
    $("#copy_image_url").select()
    document.execCommand('copy')
    alert('image copied to clipboard')
}

var elem = document.querySelector('.grid');
var msnry = new Masonry( elem, {
  // options
  itemSelector: '.grid-item',
  columnWidth: 200
});

// element argument can be a selector string
//   for an individual element
var msnry = new Masonry( '.grid', {
  // options
});

  