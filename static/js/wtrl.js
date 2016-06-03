function tags(the,num,varid,loop)
{
	if(document.getElementById(varid))
	{
		var $aryLi = document.getElementById(varid).getElementsByTagName("a");
				
		for(var i=0;i<$aryLi.length;i++)
		{
			$aryLi[i].className=""
		}
		the.className="hover";
	}
	for(var id = 1;id<=loop;id++)
	{
		var listNum = varid + id;
		var $menuid =document.getElementById(listNum);
		if(id==num)
		{
			$menuid.style.display="block";
		}
		else 
		{
			$menuid.style.display="none";
		}
	}
}

// 新闻函数
function tag(the,num,varid,loop)
{
	if(document.getElementById(varid))
	{
		var $aryLi = document.getElementById(varid).getElementsByTagName("span");
				
		for(var i=0;i<$aryLi.length;i++)
		{
			$aryLi[i].className=""
		}
		the.className="hover";
	}
	
	for(var id = 1;id<=loop;id++)
	{
		var listNum = varid + id;
		var $menuid =document.getElementById(listNum);
					
		if(id==num)
		{
			$menuid.style.display="block";
		}
		else 
		{
			$menuid.style.display="none";
		}
	}
}

// 链接函数
function linkTag(the,num,varid,loop)
{
	if(document.getElementById(varid))
	{
		var $aryLi = document.getElementById(varid).getElementsByTagName("a");
				
		for(var i=0;i<$aryLi.length;i++)
		{
			$aryLi[i].className=""
		}
		the.className="hover";
	}
	
	for(var id = 1;id<=loop;id++)
	{
		var listNum = varid + id;
		var $menuid =document.getElementById(listNum);
					
		if(id==num)
		{
			$menuid.style.display="block";
		}
		else 
		{
			$menuid.style.display="none";
		}
	}
}

