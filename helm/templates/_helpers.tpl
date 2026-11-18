{{- define "myapp.name" -}}
{{- default .Chart.Name .Values.nameOverride -}}
{{- end }}
