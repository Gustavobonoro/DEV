document.addEventListener('DOMContentLoaded', () => {

    // --- Lógica do Mouseover para os Produtos do Catálogo ---
    const productItems = document.querySelectorAll('.produto-item');
    if (productItems.length > 0) {
        productItems.forEach(item => {
            item.addEventListener('mouseover', () => {
                item.style.boxShadow = '0 8px 16px rgba(0,0,0,0.2)';
                item.style.transform = 'translateY(-5px)';
            });
            item.addEventListener('mouseout', () => {
                item.style.boxShadow = '0 2px 5px rgba(0,0,0,0.1)';
                item.style.transform = 'translateY(0)';
            });
        });
    }

    // --- Lógica do Carrossel de Imagens do Produto (na página de detalhes) ---
    const carouselContainer = document.querySelector('.carousel-container');
    if (carouselContainer) {
        const images = document.querySelectorAll('.carousel-image');
        const dots = document.querySelectorAll('.carousel-indicators .dot');
        const prevButton = document.querySelector('.carousel-button.prev');
        const nextButton = document.querySelector('.carousel-button.next');
        let currentIndex = 0;

        const showImage = (index) => {
            images.forEach(img => img.classList.remove('active'));
            dots.forEach(dot => dot.classList.remove('active'));
            images[index].classList.add('active');
            dots[index].classList.add('active');
        };

        // Garante que a primeira imagem está ativa ao carregar
        showImage(currentIndex);

        prevButton.addEventListener('click', () => {
            currentIndex = (currentIndex > 0) ? currentIndex - 1 : images.length - 1;
            showImage(currentIndex);
        });

        nextButton.addEventListener('click', () => {
            currentIndex = (currentIndex < images.length - 1) ? currentIndex + 1 : 0;
            showImage(currentIndex);
        });
        
        if (dots) {
            dots.forEach((dot, index) => {
                dot.addEventListener('click', () => {
                    currentIndex = index;
                    showImage(currentIndex);
                });
            });
        }

        // Lógica para expandir a imagem ao clicar
        const overlay = document.getElementById('overlay');
        const imagemExpandidaContainer = document.getElementById('imagem-expandida-container');
        const imagemExpandida = document.getElementById('imagem-expandida');
        const fecharImagem = document.getElementById('fechar-imagem');

        carouselContainer.addEventListener('click', (event) => {
            if (event.target.tagName === 'IMG') {
                imagemExpandida.src = event.target.src;
                overlay.style.display = 'block';
                imagemExpandidaContainer.style.display = 'block';
            }
        });

        if (fecharImagem) {
            fecharImagem.addEventListener('click', () => {
                overlay.style.display = 'none';
                imagemExpandidaContainer.style.display = 'none';
            });
        }
    
        if (overlay) {
            overlay.addEventListener('click', () => {
                overlay.style.display = 'none';
                imagemExpandidaContainer.style.display = 'none';
            });
        }
    }
    
    // --- Lógica do Botão de Ir para o Topo ---
    const btnTopo = document.getElementById('btn-topo');
    if (btnTopo) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                btnTopo.style.display = 'block';
            } else {
                btnTopo.style.display = 'none';
            }
        });
        btnTopo.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // --- Lógica do Botão do WhatsApp ---
    const botaoWhatsapp = document.getElementById('botao-whatsapp');
    if (botaoWhatsapp) {
        botaoWhatsapp.addEventListener('click', (event) => {
            event.preventDefault();
            const nomeProduto = document.querySelector('.detalhe-container h2').innerText;
            const codigoProduto = document.querySelector('.informacoes p:nth-child(3)').innerText.replace('Código:', '').trim();
            const mensagem = `Olá, gostaria de fazer um pedido!\nProduto: ${nomeProduto}\nCódigo: ${codigoProduto}`;
            const numero = '5531986030536'; // Substitua pelo número correto
            const url = `https://api.whatsapp.com/send?phone=${numero}&text=${encodeURIComponent(mensagem)}`;
            window.open(url, '_blank');
        });
    }
    
    // --- Lógica do Carrossel Automático de Banner ---
    const bannerCarousel = document.querySelector('.banner-carousel');
    if (bannerCarousel) {
        const bannerImages = document.querySelectorAll('.banner-carousel .carousel-img');
        const dots = document.querySelectorAll('.carousel-indicators .dot');
        const prevBtn = document.querySelector('.carousel-nav-btn.prev');
        const nextBtn = document.querySelector('.carousel-nav-btn.next');
        let currentBannerIndex = 0;
        let bannerInterval;

        const showBanner = (index) => {
            bannerImages.forEach(img => img.classList.remove('active'));
            dots.forEach(dot => dot.classList.remove('active'));
            bannerImages[index].classList.add('active');
            dots[index].classList.add('active');
        };

        const nextBanner = () => {
            currentBannerIndex = (currentBannerIndex + 1) % bannerImages.length;
            showBanner(currentBannerIndex);
        };

        const startBannerCarousel = () => {
            bannerInterval = setInterval(nextBanner, 5000);
        };

        const stopBannerCarousel = () => {
            clearInterval(bannerInterval);
        };

        // Garante que o carrossel inicia somente se houver imagens
        if (bannerImages.length > 0) {
            startBannerCarousel();
            showBanner(currentBannerIndex);
        }

        bannerCarousel.addEventListener('mouseover', stopBannerCarousel);
        bannerCarousel.addEventListener('mouseout', startBannerCarousel);

        if (prevBtn && nextBtn) {
            prevBtn.addEventListener('click', () => {
                stopBannerCarousel();
                currentBannerIndex = (currentBannerIndex > 0) ? currentBannerIndex - 1 : bannerImages.length - 1;
                showBanner(currentBannerIndex);
                startBannerCarousel();
            });

            nextBtn.addEventListener('click', () => {
                stopBannerCarousel();
                currentBannerIndex = (currentBannerIndex + 1) % bannerImages.length;
                showBanner(currentBannerIndex);
                startBannerCarousel();
            });
        }

        if (dots) {
            dots.forEach((dot, index) => {
                dot.addEventListener('click', () => {
                    stopBannerCarousel();
                    currentBannerIndex = index;
                    showBanner(currentBannerIndex);
                    startBannerCarousel();
                });
            });
        }
    }
});