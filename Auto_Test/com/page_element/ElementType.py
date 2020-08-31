package DataModel.PageElement;
from enum import Enum

class ElementType(Enum):
		 Input,
		 Inputcheck,
		 Link,
		 Button,
		 Dropdown,
		 UnusualDropdown,
		 Radio,
		 Checkbox,
		 DoubleClick,
		 Scroll,
		 CheckTexttobe,
		 CheckContainstext,
		 CheckValueExist,
		 CheckElementExist,
		 AlertContainer, #红绿框
		 SystemAlert

	 public static enum Statustype{ 
		NoEffect,
		Effect
		

