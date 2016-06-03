KindEditor.ready(function(K){
    K.create('textarea[name=content]',{
        width: '1000px',
        height: '550px',
        uploadJson: '/admin/upload/kindeditor'  // kindeditor上传图片的一些配置。
    });
});
