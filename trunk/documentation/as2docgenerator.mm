<map version="0.7.1">
<node COLOR="#006633" TEXT="as2docgenerator">
<node COLOR="#006633" TEXT="xml Class model" POSITION="right">
<edge WIDTH="thin"/>
<cloud COLOR="#fce3e3"/>
<font NAME="SansSerif" SIZE="12"/>
<icon BUILTIN="pencil"/>
<node TEXT="class" STYLE="bubble">
<node TEXT="attr. type (interface|class)" STYLE="fork"/>
<node TEXT="attr. name" STYLE="fork"/>
<node TEXT="attr. version" STYLE="fork"/>
<node TEXT="attr. package" STYLE="fork"/>
<node TEXT="attr. author" STYLE="fork"/>
<node COLOR="#000000" TEXT="properties" STYLE="bubble">
<node TEXT="property">
<node TEXT="attr. visibility" STYLE="fork"/>
<node TEXT="attr. type" STYLE="fork"/>
<node TEXT="attr. name" STYLE="fork"/>
</node>
</node>
<node TEXT="methods">
<node TEXT="method">
<node TEXT="attr. name" STYLE="fork"/>
<node TEXT="attr. visibility (public|private)" STYLE="fork"/>
<node TEXT="attr. modifier (static)" STYLE="fork"/>
<node TEXT="attr. returnType" STYLE="fork"/>
<node TEXT="params">
<node TEXT="param">
<node TEXT="attr. type" STYLE="fork"/>
<node TEXT="attr. name" STYLE="fork"/>
</node>
</node>
<node TEXT="description"/>
</node>
</node>
<node TEXT="description"/>
<node TEXT="detailed_description"/>
</node>
</node>
<node TEXT="documentation keywords" POSITION="left">
<icon BUILTIN="xmag"/>
<node TEXT="class related">
<icon BUILTIN="pencil"/>
<node TEXT="@name"/>
<node TEXT="@version"/>
<node TEXT="@author"/>
<node TEXT="@property"/>
<node TEXT="@see"/>
</node>
<node TEXT="methods">
<icon BUILTIN="pencil"/>
<node TEXT="@param"/>
<node TEXT="@see"/>
</node>
<node TEXT="documentation starts with /** and ends with **/&#xa;documentation must be placed ABOVE the &#xa;method/class/interface in question&#xa;---&#xa;probably a good idea to keep the special keywords&#xa;to the minimum.. description, for example, should not&#xa;require a separate @description keyword, it is the text &#xa;right after /** and lasts until the first empty line.&#xa;Example:&#xa;/**&#xa;this is some description&#xa;and this is too&#xa;&#xa;@param firstParam&#xa;**/">
<icon BUILTIN="pencil"/>
</node>
</node>
<node COLOR="#990000" TEXT="process xmlClassModel with XSL" POSITION="right">
<icon BUILTIN="xmag"/>
</node>
</node>
</map>
