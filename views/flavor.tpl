<!DOCTYPE html>
<html>
<head>
    <title>Ice Cream Flavor Picker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #fff8e7;
            text-align: center;
            padding: 50px;
        }
        h1 {
            font-size: 2em;
            color: #333;
        }
        img {
            width: 200px;
            height: auto;
            margin: 20px 0;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        p {
            font-size: 1.2em;
            color: #444;
        }
        button {
            background-color: #ffb347;
            border: none;
            padding: 12px 25px;
            font-size: 1em;
            font-weight: bold;
            color: #000;
            border-radius: 12px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #ff8c42;
        }
    </style>
</head>
<body>
    % if name:
        <h1>🍦 {{name}}</h1>
        <img src="{{img}}" alt="{{name}}">
        <p>{{desc}}</p>
    % else:
        <h1>🍦 Ice Cream Flavor Picker</h1>
        <p>{{desc}}</p>
    % end

    <form method="post">
        <button type="submit">{{btn_text}}</button>
    </form>
</body>
</html>
