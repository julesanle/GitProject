

class PageElement:
	locatorlist= list()
	def __init__(self,elementName,type,loc_type,locator,value):
		self.elementName = elementName
		self.type = type
		self.loc_type = loc_type
		self.locator = locator
		self.value = value

	def get_name(self):
		return self.elementName

	def get_locator(self):
		return self.locator

	def getvalue(self):
		return self.value
	
	def gettype(self):
		return self.type

	def get_loctype(self):
		return self.loc_type

	def  getStatus(self):
		return self.status
	
	# 单独设置字段
	def setType(self,type):
		self.type = type

	def setElementName(self, elementName):
		self.elementName = elementName

	def setlocator(self,locator):
		self.locator = locator

	def setValue(self, value):
		self.value = value

	def setStatus(self, status):
		self.status = status

	'''
	public void Input(String elementName,By elemetlocator,String value){
		this.type = Htmltype.Input;
		this.elementName = elementName;
		this.setElemetlocator(elemetlocator);
		this.value=value;
		
	}
	public void InputCheck(String elementName,By elemetlocator,Statustype status){
		this.type = Htmltype.Inputcheck;
		this.elementName = elementName;
		this.setElemetlocator(elemetlocator);
		this.status=status;
		
	}
	
	public void Button(String elementName,By elemetlocator){
		this.type =Htmltype.Button;
		this.elementName = elementName;
		this.setElemetlocator(elemetlocator);
	}
	
	public void unusualDropdown(String elementName,By elemetlocator,By elemetlocator2){
		this.type =Htmltype.UnusualDropdown;
		this.elementName = elementName;
		this.elemetlocator=elemetlocator;
		this.elemetlocator2=elemetlocator2;

	}
	public void dropdown(String elementName,By elemetlocator,By elemetlocator2,String value){
		this.type =Htmltype.Dropdown;
		this.elementName = elementName;
		this.elemetlocator=elemetlocator;
		this.elemetlocator2=elemetlocator2;
		this.value=value;
	}
	
	public void Radio(String elementName,By elemetlocator){
		this.type =Htmltype.Radio;
		this.elementName = elementName;
		this.setElemetlocator(elemetlocator);
	}
	public void Checkbox(String elementName,By elemetlocator){
		this.type =Htmltype.Checkbox;
		this.elementName = elementName;
		this.setElemetlocator(elemetlocator);
	}
	
	//红绿框
	public void alertContainer(String elementName){
		this.type = Htmltype.AlertContainer;
		this.elementName = elementName;
	}
	//系统弹框
	public void SystemAlert(String elementName){
		this.type = Htmltype.SystemAlert;
		this.elementName = elementName;
	}
	public void Scroll(String elementName,By elemetlocator){
		this.type = Htmltype.Scroll;
		this.elementName = elementName;
		this.elemetlocator=elemetlocator;
	}
	public void checkTexttobe(String elementName,By elemetlocator,String value,Statustype status){
		this.type = Htmltype.CheckTexttobe;
		this.elementName = elementName;
		this.elemetlocator=elemetlocator;
		this.value=value;
		this.status=status;
		
	}
	public void checkContainstext(String elementName,By elemetlocator,String value,Statustype status){
		this.type = Htmltype.CheckContainstext;
		this.elementName = elementName;
		this.elemetlocator=elemetlocator;
		this.value=value;
		this.status=status;
	}
	public void checkValueExist(String elementName,By elemetlocator,Statustype status){
		this.type = Htmltype.CheckValueExist;
		this.elementName = elementName;
		this.elemetlocator=elemetlocator;
		this.status=status;
	}
	public void checkElementExist(String elementName,By elemetlocator,Statustype status){
		this.type = Htmltype.CheckElementExist;
		this.elementName = elementName;
		this.elemetlocator=elemetlocator;
		this.status=status;
	}
	public void Link(String elementName,By elemetlocator){
		this.type = Htmltype.Link;
		this.elementName = elementName;
		this.elemetlocator=elemetlocator;
	}
	public void Doubleclick(String elementName,By elemetlocator){
		this.type = Htmltype.DoubleClick;
		this.elementName = elementName;
		this.elemetlocator=elemetlocator;
	}
	
	# 设置locator列表
	public List<By> locatorlist(By...arg){
		for(int i=0; i<arg.length; i++){
			locatorlist.add(arg[i]);
		}
		return locatorlist;
	}
	
	'''

