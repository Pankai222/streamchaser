<script>
    import {fly} from 'svelte/transition';
    import {
        TextField,
    } from 'svelte-materialify';
    import Footer from './components/Footer.svelte'
    import { Card } from 'framework7-svelte'

    const url = 'http://localhost:1337/search/';
    const INPUT_TIMER = 200;
    let input = '';
    let timer;
    let media = [];

    // run search if we haven't received input in the last 200ms
    const debounceInput = () => {
        clearTimeout(timer);
        timer = setTimeout(() => {
            input.trim() ? search() : media = [];
        }, INPUT_TIMER);
    }

    const search = async () => {
        const res = await fetch(url + input);
        media = await res.json();
    };

    let scale = false;

    function onMouseOver() {
        scale = 1.5;
    }

    function onMouseOut() {
    }
</script>

<main>
    <div style="padding-bottom: 3.7%">
        <div>
            <h1 style="z-index: 11">Placeholder</h1>
            <TextField dense rounded outlined autofocus
                       bind:value={input}
                       on:input={debounceInput} style="width: 30%;">
                Search
            </TextField>
        </div>
    {#if media.hits}
        <div transition:fly="{{ y: 200, duration: 200 }}"
             class="d-flex flex-wrap align-content-start mt-4 mb-4 flex-grow-0 flex-shrink-0">
            {#each media.hits as media, index}
                <div class="media-item card" class:scale on:mouseenter={debounceInput} on:mouseover={onMouseOver} on:mouseout={onMouseOut}>
                    <Card name="cardControl" class="card">
                        <img src="https://image.tmdb.org/t/p/w500{media.poster_path}" alt="background"/>
                    </Card>
                </div>
            {/each}
        </div>
    {/if}
    </div>
    <div>
        <Footer />
    </div>
</main>

<style>
    img {
        width: 100%;
        height: 100%;
    }
    .media-item {
        width: calc(14.27% - 20px);
        margin-left: 10px;
        margin-right: 10px;
        margin-top: 10px;
        height: 100%;
    }
    .card:hover {
        transition: transform 300ms linear;
        transform: scale(1.5);
        z-index: 1;
    }
</style>

