document.addEventListener('DOMContentLoaded', function() {
    const gallery = document.getElementById('gallery');
    const description = document.getElementById('description');
    const deleteModal = document.getElementById('deleteModal');
    const confirmDeleteBtn = document.getElementById('confirmDelete');
    const cancelDeleteBtn = document.getElementById('cancelDelete');
    
    let selectedItem = null;
    
    // 갤러리 아이템에 이벤트 리스너 추가
    gallery.addEventListener('click', function(e) {
        const galleryItem = e.target.closest('.gallery-item');
        if (galleryItem) {
            showDescription(galleryItem);
        }
    });
    
    // 더블클릭 이벤트 (삭제 모달)
    gallery.addEventListener('dblclick', function(e) {
        const galleryItem = e.target.closest('.gallery-item');
        if (galleryItem) {
            e.preventDefault();
            e.stopPropagation();
            showDeleteModal(galleryItem);
        }
    });
    
    // 설명 표시 함수
    function showDescription(item) {
        const desc = item.getAttribute('data-description');
        description.innerHTML = `<p>${desc}</p>`;
        
        // 선택된 아이템 스타일 변경
        document.querySelectorAll('.gallery-item').forEach(item => {
            item.style.borderColor = 'transparent';
        });
        item.style.borderColor = '#007bff';
    }
    
    // 삭제 모달 표시 함수
    function showDeleteModal(item) {
        selectedItem = item;
        deleteModal.style.display = 'block';
        
        // 모달 외부 클릭 시 닫기
        deleteModal.addEventListener('click', function(e) {
            if (e.target === deleteModal) {
                hideDeleteModal();
            }
        });
    }
    
    // 삭제 모달 숨기기 함수
    function hideDeleteModal() {
        deleteModal.style.display = 'none';
        selectedItem = null;
    }
    
    // 삭제 확인 버튼 이벤트
    confirmDeleteBtn.addEventListener('click', function() {
        if (selectedItem) {
            // 삭제 애니메이션
            selectedItem.style.transform = 'scale(0.8)';
            selectedItem.style.opacity = '0';
            
            setTimeout(() => {
                selectedItem.remove();
                hideDeleteModal();
                
                // 설명 초기화
                description.innerHTML = '<p>이미지를 클릭하면 설명이 나타납니다.</p>';
                
                // 갤러리가 비었을 때 메시지 표시
                if (gallery.children.length === 0) {
                    gallery.innerHTML = '<div style="grid-column: 1 / -1; text-align: center; padding: 50px; color: #666;">갤러리가 비었습니다.</div>';
                }
            }, 300);
        }
    });
    
    // 삭제 취소 버튼 이벤트
    cancelDeleteBtn.addEventListener('click', hideDeleteModal);
    
    // ESC 키로 모달 닫기
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && deleteModal.style.display === 'block') {
            hideDeleteModal();
        }
    });
    
    // 갤러리 아이템에 호버 효과 추가 (CSS로 처리되지만 추가적인 효과)
    gallery.addEventListener('mouseover', function(e) {
        const galleryItem = e.target.closest('.gallery-item');
        if (galleryItem) {
            galleryItem.style.transition = 'all 0.3s ease';
        }
    });
    
    // 갤러리 아이템에서 마우스가 나갈 때
    gallery.addEventListener('mouseout', function(e) {
        const galleryItem = e.target.closest('.gallery-item');
        if (galleryItem) {
            // 선택된 아이템이 아닌 경우에만 원래 스타일로 복원
            if (galleryItem.style.borderColor !== 'rgb(0, 123, 255)') {
                galleryItem.style.borderColor = 'transparent';
            }
        }
    });
    
    // 페이지 로드 시 초기 설명
    description.innerHTML = '<p>이미지를 클릭하면 설명이 나타납니다.</p>';
}); 