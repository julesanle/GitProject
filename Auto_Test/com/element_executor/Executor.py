


class Executor：
	private Input input=new Input();
	private Select select=new Select();
	private Scroll scroll=new Scroll();
	private RadioCheckBox radiocheck=new RadioCheckBox();
	private Click click=new Click();
	private DoubleClick doubleclick=new DoubleClick();
	private Checkelement checkelement=new Checkelement();
	private GetElement getelement=new GetElement();
	private Log log=new Log();
	private String screenPath;
	public  boolean executor(WebDriver driver,List<PageElement> ListElement,String policyNum){
		File directory =new File("test-output") ;
    	try {
			screenPath=directory.getCanonicalPath() + "/img/";
		} catch (IOException e) {
			e.printStackTrace();
		}
		boolean executor=true;
		for(PageElement element:ListElement){
			Htmltype elementType=element.gettype();
			String elementName=element.getElementName();
			String elementValue=element.getvalue();
			Statustype status=element.getStatus();
			//非校验的input,输入值
			if(elementType.equals(Htmltype.Input)){
				if(!input.InputKeys(driver, element)){
					log.WriteWronglog(driver,screenPath,policyNum+elementName+"：输入失败");
				}
			}
			//校验input,点击该input校验是否有值,不影响流程-影响流程
			else if(elementType.equals(Htmltype.Inputcheck)){
				if(!input.InputCheck(driver, element)){
					log.WriteWronglog(driver,screenPath,policyNum+elementName+"无数据");	
					if(status.equals(Statustype.Effect)){
						executor=false;
						break;	
					}	
				}
			}
			//Button Link 执行点击操作
			else if(elementType.equals(Htmltype.Button)||elementType.equals(Htmltype.Link)){
				click.clickelement(driver,element.getElemetlocator(), elementName);
			}
			//支持模糊查询的Select 执行下拉列表选择操作
			else if(elementType.equals(Htmltype.Dropdown)){
				if(!select.dropDownManage(driver,element)){
					log.WriteWronglog(driver,screenPath,policyNum+elementName+"选择数据失败");
					executor=false;
					break;
				}
			}
			//不带模糊查询的select， 执行下拉列表选择操作
			else if(elementType.equals(Htmltype.UnusualDropdown)){
				if(!select.unusualDropDownManage(driver,element)){
					log.WriteWronglog(driver,screenPath,policyNum+elementName+"选择数据失败");
					executor=false;
					break;
				}
			}
			//Checkbox、Radio，执行点击操作
			else if(elementType.equals(Htmltype.Radio)||elementType.equals(Htmltype.Checkbox)){
				radiocheck.RadioCheckBoxClick(driver, element);
			}
			
			//DoubleClick,进行双击操作
			else if(elementType.equals(Htmltype.DoubleClick)){
				doubleclick.clickelement(driver,element.getElemetlocator(),elementName);
			}
			//Scroll用于滚动至页面元素可见
			else if(elementType.equals(Htmltype.Scroll)){
				scroll.scrollToElement(driver, element);
			}
			//判断元素值是否为给定的值
			else if(elementType.equals(Htmltype.CheckTexttobe)){
				if(!checkelement.WaitelementtextToBe(driver,60,element.getElemetlocator(),elementValue)){
					log.WriteWronglog(driver, screenPath,"未找到值为："+elementValue+"的"+elementName);
					if(status.equals(Statustype.Effect)){
						executor=false;
						break;
					}
				}
			}
				
			//判断元素值是否包含给定的值
			else if(elementType.equals(Htmltype.CheckContainstext)){
				if(!checkelement.WaitelementContainstext(driver,60,element.getElemetlocator(), elementValue)){
					log.WriteWronglog(driver,screenPath,policyNum+elementName+"不包含值："+elementValue);
					if(status.equals(Statustype.Effect)){
						executor=false;
						break;
					}
				}
			}
			//判断元素是否有值
			else if(elementType.equals(Htmltype.CheckValueExist)){
				if(!checkelement.isvalue(driver,20,element.getElemetlocator(),element.getElementName())){
					log.WriteWronglog(driver,screenPath,policyNum+elementName+"元素值不存在");
					if(status.equals(Statustype.Effect)){
						executor=false;
						break;
					}
				}
			}
			//判断元素是否存在
			else if(elementType.equals(Htmltype.CheckElementExist)){
				if(!checkelement.Waitelement(driver,20,element.getElemetlocator())){
					log.WriteWronglog(driver,screenPath,policyNum+elementName+"元素不存在");
					if(status.equals(Statustype.Effect)){
						executor=false;
						break;
					}
				}
			}
			//红绿框
			else if(elementType.equals(Htmltype.AlertContainer)){
				if(!getelement.Getalert(driver,elementName)){
					log.WriteWronglog(driver,screenPath,policyNum+"提交失败");
					executor=false;
					break;
				}
			}
			//判断是否有系统弹窗，若存在全部关闭
			else if(elementType.equals(Htmltype.SystemAlert)){
				checkelement.acceptallalert(driver);
			}
			else{
				//其他可能出现的操作
			}
		}
		return executor;
	}
}
