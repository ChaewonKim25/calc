html = b"""
<html>
    <body>
        <form oninput="sum.value=parseInt(a.value)+parseInt(b.value),product.value=parseInt(a.value)*parseInt(b.value)">
            a = <input type="number" name="a"> 
            b = <input type="number" name="b"><br><br>
            <input type="submit">
            Sum: <output name="sum" for="a b"></output>
            Product:<output name="product" value="parseInt(a.value)*parseInt(b.value)"></output>
        </form>
    </body>
"""
