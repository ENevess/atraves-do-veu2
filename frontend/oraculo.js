async function enviarMensagem() {
    const entrada = document.getElementById("entrada").value.trim();
    if (!entrada) return;

    const respostaBox = document.getElementById("dialogo");
    const listaHistorico = document.getElementById("lista-historico");

    respostaBox.innerHTML = "<em>Consultando o Oráculo...</em>";

    try {
        const resposta = await fetch("/interagir", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ mensagem: entrada })
        });

        const dados = await resposta.json();
        const respostaTexto = dados.resposta || "O Oráculo não respondeu.";

        setTimeout(() => {
            respostaBox.innerText = respostaTexto;

            const item = document.createElement("li");
            item.innerHTML = "<strong>Você:</strong> " + entrada + "<br><strong>Oráculo:</strong> " + respostaTexto;
            listaHistorico.prepend(item);

            document.getElementById("entrada").value = "";

            if (dados.encerrar) {
                document.getElementById("entrada").disabled = true;
            }
        }, 1000);

    } catch (error) {
        respostaBox.innerText = "Erro ao consultar o Oráculo.";
        console.error(error);
    }
}
