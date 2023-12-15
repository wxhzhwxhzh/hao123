



// 所有class="link-3"  的<a>标签的属性变成  target="_blank" rel="nofollow"
var link3Elements = document.querySelectorAll('a.link-3');
// 遍历所有选中的<a>标签
for (var i = 0; i < link3Elements.length; i++) {
    var link = link3Elements[i];
    // 设置target属性为"_blank"
    link.setAttribute('target', '_blank');
    // 设置rel属性为"nofollow"
    link.setAttribute('rel', 'nofollow');
}
var icoElements = document.querySelectorAll('img.ico');





// 遍历所有选中的<img>标签  设置高与宽
var size='15px'
for (var i = 0; i < icoElements.length; i++) {
    var link = icoElements[i];
    
    link.setAttribute('height', size);
    
    link.setAttribute('width', size);
}




// 获取所有id为"vip"的<a>标签
var vipElements = document.querySelectorAll('a#vip');

// 遍历所有选中的<a>标签
for (var i = 0; i < vipElements.length; i++) {
    var link = vipElements[i];
    // 设置文本颜色为红色
    link.style.color = 'pink';
}




//切换皮肤
document.getElementById("skin").addEventListener("click", function (event) {
    event.preventDefault(); // 阻止链接的默认行为
    if (document.body.style.backgroundImage != "none") {

        document.body.style.backgroundImage = "none"; // 移除背景图片
        document.body.style.backgroundColor = "#232328"; // 修改背景颜色
        
    } else {
        document.body.style.backgroundImage = "url(img/01.jpg)";				

    }

});