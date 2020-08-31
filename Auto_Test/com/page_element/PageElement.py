package DataModel.PageElement;

import java.util.ArrayList;
import java.util.List;

import org.openqa.selenium.By;

import DataModel.PageElement.ElementType.Htmltype;
import DataModel.PageElement.ElementType.Statustype;


public class PageElement {
	locatorlist=ArrayList<By>();
	private By elemetlocator;
	private By elemetlocator2;
	private String value;
	private Statustype status;
	public PageElement(){}
	
	public String getElementName() {
		return elementName;
	}
	public List<By> getlocatorlist() {
		return locatorlist;
	}
	public String getvalue() {
		return value;
	}
	
	public Htmltype gettype() {
		return type;
	}
	public By getElemetlocator() {
		return elemetlocator;
	}
	public By getElemetlocator2() {
		return elemetlocator2;
	}
	public Statustype getStatus() {
		return status;
	}

	
	# 单独设置字段
	public void setType(Htmltype type) {
		this.type = type;
	}
	public void setElementName(String elementName) {
		this.elementName = elementName;
	}
	public void setlocator(List<By> locator) {
		this.locatorlist = locator;
	}
	public void setValue(String value) {
		this.value = value;
	}
	public void setElemetlocator(By elemetlocator) {
		this.elemetlocator = elemetlocator;
	}
	public void setElemetlocator2(By elemetlocator2) {
		this.elemetlocator2 = elemetlocator2;
	}
	public void setStatus(Statustype status) {
		this.status = status;
	}
	
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


	
	
}
