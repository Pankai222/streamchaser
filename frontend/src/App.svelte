<script>
    import { fade, fly } from 'svelte/transition';
    import { MaterialApp, Button, Card, CardText, CardActions } from 'svelte-materialify';

    let input = "";
    let output = [];
    let data = [];
    const search = async (input) => {
        try {
            data = await ( await fetch(`http://localhost:1337/search/${input}`)).json();
            console.log(data.hits);
            if (data && data.hits) {
                console.log(data.hits);
            }
            console.log();
        } catch (e) {
            console.error(e);
        }
    };

</script>

<main>
    <div id="data_table" />

    <h1>Input {input}!</h1>

    <input bind:value={input} on:input={search(input)}/>
    <Button class="primary-color">
        It actually fucking works now! :^)
    </Button>

    <div class="d-flex justify-center mt-4 mb-4">
  <Card outlined style="max-width:300px;">
    <div class="pl-4 pr-4 pt-3">
      <span class="text-overline"> OVERLINE </span>
      <br />
      <span class="text-h5 mb-2">Movie!</span>
      <br />
    </div>
    <CardText>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit, qui quaerat
      rerum incidunt nisi ducimus?
    </CardText>
    <CardActions>
      <Button rounded outlined>Button</Button>
    </CardActions>
  </Card>
</div>

    {#if data.hits}
        <table>
            <tr>
                <th transition:fly="{{y: 200, duration: 2000}}">ID</th>
                <th transition:fly="{{y: 200, duration: 2000}}">Title</th>
                <th transition:fly="{{y: 200, duration: 2000}}">Release Date</th>
                <th transition:fly="{{y: 200, duration: 2000}}">Genres</th>
            </tr>
        {#each data.hits as movie}
            <tr>
                <td transition:fly="{{y: 200, duration: 2000}}">{movie.id}</td>
                <td transition:fly="{{y: 200, duration: 2000}}">{movie.title}</td>
                <td transition:fly="{{y: 200, duration: 2000}}">{movie.release_date}</td>
                <td transition:fly="{{y: 200, duration: 2000}}">{movie.genres}</td>
            </tr>
        {/each}
        </table>
    {/if}
</main>

<style>
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;
    }

    h1 {
        color: #ff3e00;
        text-transform: uppercase;
        font-size: 4em;
        font-weight: 100;
    }

    th, td {
        padding: 15px;
        text-align: left;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
</style>
