<template>
    <header>
        <ul class=" m-0 p-0 text-white d-flex align-items-center flex-column ">
            <li class="">
                <RouterLink class="fs-3" to="/">Home</RouterLink>
            </li>
            <li>
                <RouterLink to="/books">books</RouterLink>
            </li>
        </ul>
    </header>
</template>
<style scoped>
    ul{
        list-style: none;

    }
    ul li{
        text-decoration: none;
    }

</style>