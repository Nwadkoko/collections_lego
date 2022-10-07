%rebase('base.tpl')
<header>
    <h1>My LEGO's Collection</h1>
</header>
<main>

    <form class="add-item" action="/add" method="POST">
        <input type="text" name="item" placeholder="49083-1">
        <button type="submit">Add</button>
    </form>

    <ol>
        %for item in items:
        <li>
            <div class="img-container">
                <img src="{{item[5]}}">
            </div>
            <div class="text-btn-container">
                <h2>{{item[1]}}</h2>
                <div class="btn-container">
                    <a href="https://brickset.com/sets/{{item[0]}}" target="_blank"><i class="fa fa-link"></i></a>
                    <a href="/lego.csv/remove/{{item[0]}}"><i class="fa fa-trash"></i></a>
                </div>
            </div>
        </li>
        %end
    </ol>
</main>