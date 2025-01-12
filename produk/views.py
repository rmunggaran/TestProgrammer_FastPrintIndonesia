from django.shortcuts import render, get_object_or_404, redirect
from .models import Produk,Kategori, Status
from .serializers import ProdukSerializer
from django.contrib import messages

def produk_list(request):
    statuses = Status.objects.all()

    status_filter = request.GET.get('status')
    
    if status_filter:
        produk = Produk.objects.filter(status_id=status_filter).order_by('-id')
    else:
        produk = Produk.objects.all().order_by('-id') 

    return render(request, 'produk/produk_list.html', {
        'produk': produk,
        'statuses': statuses,
        'title': 'Daftar Produk'
    })

def produk_create(request):
    kategoris = Kategori.objects.all()
    statuses = Status.objects.all()

    if request.method == 'POST':
        kategori_id = request.POST.get('kategori_id')
        nama_produk = request.POST.get('nama_produk')
        harga = request.POST.get('harga')
        status_id = request.POST.get('status_id')
        
        if not kategori_id or not nama_produk or not harga or not status_id:
            messages.error(request, 'Semua field harus diisi dengan benar.')
            return render(request, 'produk/produk_form.html')
        else:
            try:
                Produk.objects.create(
                    nama_produk=nama_produk,
                    harga=harga,
                    kategori_id=kategori_id,
                    status_id=status_id
                )
                messages.success(request, 'Produk berhasil ditambahkan.')
                return redirect('produk_list')

            except Exception as e:
                messages.error(request, f'Terjadi kesalahan saat menambahkan produk: {str(e)}')
                return render(request, 'produk/create.html')
    
    return render(request, 'produk/produk_form.html', {'kategoris': kategoris, 'statuses': statuses, 'title': 'From Tambah Produk'})

def produk_edit(request, id):
    produk = get_object_or_404(Produk, id=id)
    kategoris = Kategori.objects.all()
    statuses = Status.objects.all()

    if request.method == 'POST':
        produk.nama_produk = request.POST.get('nama_produk')
        produk.harga = request.POST.get('harga')
        produk.kategori_id = request.POST.get('kategori_id')
        produk.status_id = request.POST.get('status_id')

        if not produk.nama_produk or not produk.harga or not produk.kategori_id or not produk.status_id:
            messages.error(request, 'Semua field harus diisi dengan benar.')
            return render(request, 'produk/produk_form.html', {
                'produk': produk,
                'kategoris': kategoris,
                'statuses': statuses
            })

        try:
            produk.save()
            messages.success(request, 'Produk berhasil diperbarui.')
            return redirect('produk_list')

        except Exception as e:
            messages.error(request, f'Terjadi kesalahan saat memperbarui produk: {str(e)}')
            return render(request, 'produk/produk_form.html', {
                'produk': produk,
                'kategoris': kategoris,
                'statuses': statuses
            })


    return render(request, 'produk/produk_form.html', {
        'produk': produk,
        'kategoris': kategoris,
        'statuses': statuses
    })

def produk_delete(request, id):
    produk = get_object_or_404(Produk, id=id)
    
    if request.method == 'POST':
        try:
            produk.delete()
            messages.success(request, 'Produk berhasil dihapus.')
            return redirect('produk_list')

        except Exception as e:
            messages.error(request, f'Terjadi kesalahan saat menghapus produk: {str(e)}')
            return redirect('produk_list')

    return redirect('produk_list')