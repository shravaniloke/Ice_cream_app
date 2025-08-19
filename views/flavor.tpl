<!DOCTYPE html>
<html>
<head>
    <title>Ice Cream Flavor Picker</title>
    <style>
        body { text-align: center; font-family: Arial; background-color: #fff8e1; }
        img { max-width: 300px; border-radius: 20px; margin-top: 15px; }
        button { padding: 10px 20px; font-size: 18px; background: #ffcc80; border: none; border-radius: 10px; cursor: pointer; }
        button:hover { background: #ffb74d; }
    </style>
</head>
<body>
    <h1>{{'🍦 ' + name if name else 'Ice Cream Flavor Picker'}}</h1>

    % if img:
        <img src="/static/{{img}}" alt="{{name}}">
    % end

    <p>{{desc}}</p>

    <form action="/" method="post">
        <button type="submit">{{btn_text}}</button>
    </form>
</body>
</html>
