using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class FrmNuevoUsuario : Form
    {

        bool IsNuevo = false;
        public FrmNuevoUsuario()
        {
            InitializeComponent();
        }

        private void label8_Click(object sender, EventArgs e)
        {
            this.Hide();
        }

        private void FrmNuevoUsuario_Load(object sender, EventArgs e)
        {
            this.botones();
            this.habilitar(false);
        }

        //metodo habilitar 
        private void habilitar(bool valor)
        {

            this.txtId.ReadOnly = !valor;
            this.txtNombre.ReadOnly = !valor;
            this.txtApellido.ReadOnly = !valor;
            this.dtpFechaN.Enabled = valor;
            this.txtUsuario.ReadOnly = !valor;
            this.txtPass.ReadOnly = !valor;
        }

        //metodo limpiar
        private void limpiar()
        {
            this.txtId.Clear();
            this.txtNombre.Clear();
            this.txtApellido.Clear();
            this.txtUsuario.Clear();
            this.txtPass.Clear();
        }


        //Método botones
        private void botones()
        {
            if (this.IsNuevo)
            {
                habilitar(true);
                this.btnNuevo.Enabled = false;
                this.btnGuardar.Enabled = true;
                this.btnCancelar.Enabled = true;
            }
            else
            {
                habilitar(false);
                this.btnNuevo.Enabled = true;
                this.btnGuardar.Enabled =false;
                this.btnCancelar.Enabled = false;
            }
        }

        private void btnNuevo_Click(object sender, EventArgs e)
        {
            IsNuevo = true;
            this.habilitar(true);
            botones();
            
        }

        private void btnCancelar_Click(object sender, EventArgs e)
        {
            IsNuevo = false;
            this.habilitar(false);
            botones();
            limpiar();
        }
    }
}
