<template>
    <section>
        <div>
            <h1>We're here to help you navigate</h1>
            <h1>the road ahead</h1>
            <h4>Get practical tips and tools for COVID-19</h4>
            <button>Explore</button>
        </div>

        <img src="@/assets/job-search.svg" alt="person working">

    </section>
</template>

<script>
export default {
    name: "infoBar"
}
</script>

<style lang="scss" scoped>

section {
    background: var(--info);
    padding: 50px 200px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;

    & > img {
        height: 350px;
        width: auto;
        
    }

    & > div {
        padding-top: 30px;
        color: var(--primary);

        & > h4 {
            margin-top: 10px;
            font-weight: 200;
        }

        & > button {
            background: var(--primary);
            color: white;
            border: none;
            padding: 12px;
            margin-top: 12px;
            font-size: 18px;
            border-radius: 3px;
        }
    }
}

@media all and (max-width: 740px) {
    section {
        display: block;
        text-align: center;

        & > img {
            margin-left: -40px;
            min-width: 340px;
            height: auto;
        }

        & > div {
            text-align: center;
            margin-bottom: 20px;
        }
    }
}

</style>