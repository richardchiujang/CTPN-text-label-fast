# CTPN-use-labelImg-text-label-fast

reqiured :
labelImg tool 

https://github.com/tzutalin/labelImg.git



because the endless labeling CTPN text labels , this code will split large (long) rectbox into small 15 pix width rectbox 
that all the text label need

因為標註CTPN資料標籤需要不斷的框出15像素寬的文字框，標註大量文字框的時候非常痛苦與無奈，所以這支程式可以將長的文字框，切割成寬度15的文字框

說明 :
程式會將標註為 textbox 的文字框都切割，但是標註為 text 的都不會動，而且只會做 VOC 格式的 XML，因為我只需要這個

<div>
    <img src="https://github.com/richardchiujang/CTPN-use-labelImg-text-label-fast/blob/master/2020-06-05-001.JPG" width="100%">
</div>
<div>
    <img src="https://github.com/richardchiujang/CTPN-use-labelImg-text-label-fast/blob/master/2020-06-05-002.JPG" width="100%">
</div>
<div>
    <img src="https://github.com/richardchiujang/CTPN-use-labelImg-text-label-fast/blob/master/2020-06-05-003.JPG" width="100%">
</div>
<div>
    <img src="https://github.com/richardchiujang/CTPN-use-labelImg-text-label-fast/blob/master/2020-06-05-004.JPG" width="100%">
</div>
<div>
    <img src="https://github.com/richardchiujang/CTPN-use-labelImg-text-label-fast/blob/master/2020-06-05-005.JPG" width="100%">
</div>
<div>
    <img src="https://github.com/richardchiujang/CTPN-use-labelImg-text-label-fast/blob/master/2020-06-05-006.JPG" width="100%">
</div>
<div>
    <img src="https://github.com/richardchiujang/CTPN-use-labelImg-text-label-fast/blob/master/2020-06-05-007.JPG" width="100%">
</div>


