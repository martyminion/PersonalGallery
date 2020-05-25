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


$(document).ready(function()
{
  $("#copyimg").click(function(){
    alert('image copied to clipboard')
  })

  });