%rebase('base.tpl')
<header>
    <h1>My LEGO's Collection</h1>
</header>
<main>

    <form class="add-item" action="/add" method="POST">
        <input type="text" name="item" placeholder="49083-1">
        <button type="submit">Add</button>
    </form>

    %for item in items:
    <h2 class="minifig-collection-heading">{{item[0]}}</h2>
    <ol>
        %for minifig in item[1]:
        <li>
            <div class="img-container">
                <img src="{{minifig[5]}}">
            </div>
            <div class="text-btn-container">
                <h2>{{minifig[1]}}</h2>
                <div class="btn-container">
                    <a href="https://brickset.com/sets/{{minifig[0]}}" target="_blank"><i class="fa fa-link"></i></a>
                    <a href="/lego.csv/remove/{{minifig[0]}}"><i class="fa fa-trash"></i></a>
                </div>
            </div>
        </li>
        %end
        %end
    </ol>
</main>