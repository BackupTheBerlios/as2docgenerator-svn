import MYClass;

/**
* @class StringTokenizer
* @author Joe Coder
* @version 0.5
* @description Implements the behaviour of Java StringTokenizer Class<p>
*		Constructs a string tokenizer for the specified string. The
*		characters in the <code>delim</code> argument are the delimiters
*		for separating tokens. Delimiter characters themselves will not
*		be treated as tokens.
*
*		The set of delimiters (the characters that separate tokens) may
*		be specified either at creation time or on a per-token basis.
*		<p>
*		A <tt>StringTokenizer</tt> object internally maintains a current
*		position within the string to be tokenized. Some operations advance this
*		current position past the characters processed.<p>
*		A token is returned by taking a substring of the string that was used to
*		create the <tt>StringTokenizer</tt> object.
*		<p>
*		The following is one example of the use of the tokenizer. The code:
*		<blockquote><pre>
*		st:StringTokenizer  = new StringTokenizer("this is a test");
*		while (st.hasMoreTokens()) {
*			trace(st.nextToken());
*		}
*		</pre></blockquote>
*		<p>
*		prints the following output:
*		<blockquote><pre>
*		this
*		is
*		a
*		test
*		</pre></blockquote>
* @usage   <pre>myTokenizer = new StringTokenizer(str[, delim])</pre>
* @param   str  (String)   a string to be parsed.
* @param   delim (String)  the delimiters.
*/

class StringTokenizer
{
	/**
	* @property anotherProp
	* @property someProp (String) Not sure what's it for.
	* @property otherProp (Number) Not sure either. Looks nice, though.
	*@property yetAnotherProp (Object) plain Object. really useless.
	*/
	private var _string:String;
	private var _delimiters:String;
	private var _currPosition:Number;
	private var _newPosition:Number;
	private var _maxPosition:Number;
	private var _delimitersChanged:Boolean;

	public function StringTokenizer(str:String, delim:String){
		_string = str;
		_delimiters = (delim) ? delim : " \t\n\r\f";
		_currPosition = 0;
		_newPosition = -1;
		_maxPosition = _string.length;
		_delimitersChanged = false;

	}
	/**
	* @method hasMoreTokens
	* @description  Tests if there are more tokens available from this tokenizer's string.
	*		If this method returns <tt>true</tt>, then a subsequent call to
	*		<tt>nextToken</tt> with no argument will successfully return a token.
	* @usage <code>StringTokenizer.hasMoreTokens()</code>
	* @returns  <code>true</code> if and only if there is at least one token
	*          in the string after the current position; <code>false</code>
	*          otherwise.
	*/
	public function hasMoreTokens():Boolean{
		return true;
	}

	/**
	* @method nextToken
	* @description  Returns the next token in this string tokenizer's string. First,
	*		the set of characters considered to be delimiters by this
	*		<tt>StringTokenizer</tt> object is changed to be the characters in
	*		the string <tt>delim</tt>. Then the next token in the string
	*		after the current position is returned. The current position is
	*		advanced beyond the recognized token.  The new delimiter set
	*		remains the default after this call.
	* @usage <code>StringTokenizer.nextToken(delim)</code>
	* @param delim (String) the new delimiters.
	* @return String - The next token after switching to the new delimiter set.
	* @throws  NoSuchElementError  if there are no more tokens in this
	*               tokenizer's string.
	*/
	public function nextToken(delim:String):String{
		var s=new String("test");
		if (s==undefined) {
			throw new NoSuchElementError("no more tokens");
		} else {
			return s;
		}
	}
	/**
	* @method countTokens
	* @description  Calculates the number of times that this tokenizer's
	*		<code>nextToken</code> method can be called before it generates an
	*		exception. The current position is not advanced.
	* @usage <code>StringTokenizer.countTokens()</code>
	* @returns Number - tokens remaining in the string using the current delimiter set.
	*/
	public function countTokens():Number{
		var n = 1;
		return n;
	}

	private function scanTokens(){
	}

}