# Generated by Django 3.1.4 on 2021-02-23 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamentoinstancia',
            name='agendamentoHorario',
            field=models.TimeField(default='', verbose_name='Horário:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agendamentoinstancia',
            name='agendamentoAeronave',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.aeronave', verbose_name='Selecione a aeronave:'),
        ),
        migrations.AlterField(
            model_name='agendamentoinstancia',
            name='agendamentoBaseAerea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.cidades', verbose_name='Base aérea:'),
        ),
        migrations.AlterField(
            model_name='agendamentoinstancia',
            name='agendamentoData',
            field=models.DateField(verbose_name='Data:'),
        ),
        migrations.AlterField(
            model_name='agendamentoinstancia',
            name='agendamentoInstrutor1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instrutor_1', to='app1.perfil', verbose_name='Instrutor 1:'),
        ),
        migrations.AlterField(
            model_name='agendamentoinstancia',
            name='agendamentoInstrutor2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instrutor_2', to='app1.perfil', verbose_name='Instrutor 2:'),
        ),
        migrations.AlterField(
            model_name='agendamentoinstancia',
            name='agendamentoPerfil',
            field=models.ForeignKey(help_text='Instrutor.', on_delete=django.db.models.deletion.CASCADE, related_name='Perfil', to='app1.perfil', verbose_name='Perfil:'),
        ),
        migrations.AlterField(
            model_name='agendamentoinstancia',
            name='agendamentoStatus',
            field=models.CharField(blank=True, choices=[('e', 'Em curso.'), ('c', 'Cancelado!'), ('a', 'Atrasado.'), ('r', 'Reservado.'), ('f', 'Concluído.'), ('m', 'Em requisição')], default='m', help_text='Estado do agendamento.', max_length=1),
        ),
    ]
