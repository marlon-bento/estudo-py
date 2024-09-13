<template>
    <header class="h-100">
        <div class="d-flex align-items-center m-2">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                    class="icon icon-tabler icons-tabler-outline icon-tabler-books custom-icon-menu">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                    <path d="M5 4m0 1a1 1 0 0 1 1 -1h2a1 1 0 0 1 1 1v14a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1z" />
                    <path d="M9 4m0 1a1 1 0 0 1 1 -1h2a1 1 0 0 1 1 1v14a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1z" />
                    <path d="M5 8h4" />
                    <path d="M9 16h4" />
                    <path
                        d="M13.803 4.56l2.184 -.53c.562 -.135 1.133 .19 1.282 .732l3.695 13.418a1.02 1.02 0 0 1 -.634 1.219l-.133 .041l-2.184 .53c-.562 .135 -1.133 -.19 -1.282 -.732l-3.695 -13.418a1.02 1.02 0 0 1 .634 -1.219l.133 -.041z" />
                    <path d="M14 9l4 -1" />
                    <path d="M16 16l3.923 -.98" />
            </svg>
            <span class="text-logo fs-1">Locallibrary</span>
            
        </div>
        <ul class=" m-0 p-0 text-white d-flex align-items-center flex-column h-100 justify-content-center">
            <li class=" d-flex align-items-center">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                    class="icon icon-tabler icons-tabler-outline icon-tabler-home custom-icon-menu">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                    <path d="M5 12l-2 0l9 -9l9 9l-2 0" />
                    <path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7" />
                    <path d="M9 21v-6a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v6" />
                </svg>
                <RouterLink class="link bg-gray-50" to="/">Home</RouterLink>
            </li>
            <li class=" d-flex align-items-center">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                    class="icon icon-tabler icons-tabler-outline icon-tabler-books custom-icon-menu">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                    <path d="M5 4m0 1a1 1 0 0 1 1 -1h2a1 1 0 0 1 1 1v14a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1z" />
                    <path d="M9 4m0 1a1 1 0 0 1 1 -1h2a1 1 0 0 1 1 1v14a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1z" />
                    <path d="M5 8h4" />
                    <path d="M9 16h4" />
                    <path
                        d="M13.803 4.56l2.184 -.53c.562 -.135 1.133 .19 1.282 .732l3.695 13.418a1.02 1.02 0 0 1 -.634 1.219l-.133 .041l-2.184 .53c-.562 .135 -1.133 -.19 -1.282 -.732l-3.695 -13.418a1.02 1.02 0 0 1 .634 -1.219l.133 -.041z" />
                    <path d="M14 9l4 -1" />
                    <path d="M16 16l3.923 -.98" />
                </svg>
                <RouterLink class="link " to="/books">books</RouterLink>
            </li>
        </ul>
    </header>
</template>
<style scoped>

ul {
    list-style: none;

}

ul li {
    text-decoration: none;
}
.link {
  color: white; /* Exemplo de cor */
  font-size: 24px;
  
}
.link:hover {
  color: rgb(24, 22, 22); /* Exemplo de cor */
  
}
.text-logo{
    color: var(--cor-padrao-menu);
}
svg {

    color: var(--cor-padrao-menu);
    width: var(--tamanho-icons-menu);
    height: var(--tamanho-icons-menu);
    stroke-width: 1px;
}
</style>